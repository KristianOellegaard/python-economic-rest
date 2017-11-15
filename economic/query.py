import urlparse

from economic.utils import economic_request


class QueryMixin(object):
    @classmethod
    def _query(cls, auth, base_url, page_size=1000, limit=None, reverse=False, filters=None, sorting=None, timeout=60):
        assert page_size <= 1000, "Max 1000 items per page allowed. The generator will automatically fetch extra pages."
        if limit is not None:
            assert isinstance(limit, int), "limit argument must be an integer, it is %s" % type(limit)

        request_params = {
            'pagesize': page_size,
            'skippages': 0
        }
        if limit and limit < page_size:
            request_params['pagesize'] = limit  # slight optimization

        # construct the filter parameter
        if not filters:
            filters = {}
        for fltr, value in filters.items():
            if 'filter' not in request_params:
                request_params['filter'] = u''
            if request_params['filter']:
                request_params['filter'] = u'%s$and:' % request_params['filter']
            fltr = fltr.split('__')
            if len(fltr) == 1:
                field = fltr[0]
                operator = 'eq'
            elif len(fltr) == 2:
                field, operator = fltr
            else:
                raise NotImplementedError(u'Invalid filter "%s"!' % fltr)
            request_params['filter'] += u'%s$%s:%s' % (field, operator, value)

        if sorting:
            if isinstance(sorting, (list, tuple)):
                request_params['sort'] = ','.join(sorting)
            else:
                request_params['sort'] = sorting

        # make the queries
        items_returned = 0
        if reverse:
            # an extra query is required when using reverse so we can determine the last page
            reverse_request_params = request_params.copy()
            reverse_request_params['pagesize'] = 1  # make a fast query
            request = economic_request(auth, base_url, request_params=reverse_request_params, timeout=timeout)
            total_items = request['pagination']['results']
            if not limit or limit > total_items:
                limit = total_items
            last_page = total_items / page_size
            page = last_page
            page_direction = -1
        else:
            page = 0
            page_direction = 1

        while limit is None or items_returned < limit:
            request_params['skippages'] = page
            request = economic_request(auth, base_url, request_params=request_params, timeout=timeout)
            total_items = request['pagination']['results']
            if limit is None or limit > total_items:
                limit = total_items
            for itm in reversed(request['collection']) if reverse else request['collection']:
                if items_returned < limit:
                    items_returned += 1
                    yield cls(auth, itm)
                else:
                    break
            page += page_direction

    @classmethod
    def all(cls, auth, page_size=1000, limit=None, reverse=False, timeout=60):
        """
        Returns a generator that on-demand fetches `limit` number of items, at max `page_size` at a time.
        """
        return cls._query(auth, cls.base_url, page_size=page_size, limit=limit, reverse=reverse, timeout=timeout)

    @classmethod
    def filter(cls, auth, base_url=None, page_size=1000, limit=None, reverse=False, timeout=60, sorting=None, **kwargs):
        """
        Returns a generator that on-demand fetches `limit` number of items, at max `page_size` at a time.

        Additional keyword arguments can be passed to filter the list, for example:
            .filter(name="Joe", last_name__eq="Smith", city__like="*port", age__lte=40)

        See the e-conomic API for available operators.
        """
        if not base_url:
            base_url = cls.base_url
        filters = {kwarg: val for kwarg, val in kwargs.items()}
        return cls._query(auth, base_url, page_size=page_size, limit=limit, reverse=reverse, filters=filters, sorting=sorting, timeout=60)

    @classmethod
    def get(cls, auth, object_id, timeout=60, **kwargs):
        """
        Returns one item with the specified ID.
        """
        request = economic_request(auth, urlparse.urljoin(cls.base_url, unicode(object_id)), timeout=timeout)
        return cls(auth, request)
