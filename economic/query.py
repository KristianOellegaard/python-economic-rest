from economic.utils import economic_request


class QueryMixin(object):
    @classmethod
    def _query(cls, auth, base_url, page_size=1000, limit=None, reverse=False):
        assert page_size <= 1000, "Max 1000 items per page allowed. The generator will automatically fetch extra pages."

        request = economic_request(auth, base_url, page_size=page_size, skip_pages=0)
        total_items = request['pagination']['results']
        if not limit or limit > total_items:
            limit = total_items
        last_page = total_items / page_size
        items_returned = 0

        if reverse:
            page = last_page
            page_direction = -1
        else:
            page = 0
            page_direction = 1

        while items_returned < limit:
            request = economic_request(auth, base_url, page_size=page_size, skip_pages=page)
            total_items = request['pagination']['results']
            if limit > total_items:
                limit = total_items
            for itm in reversed(request['collection']) if reverse else request['collection']:
                if items_returned < limit:
                    items_returned += 1
                    yield cls(auth, itm)
                else:
                    break
            page += page_direction

    @classmethod
    def all(cls, auth, page_size=1000, limit=None, reverse=False):
        """
        Returns a generator that on-demand fetches `limit` number of items, at max `page_size` at a time.
        """
        return cls._query(auth, cls.base_url, page_size=page_size, limit=limit, reverse=reverse)

    @classmethod
    def filter(cls, auth, page_size=1000, limit=None, reverse=False, **kwargs):
        """
        Returns a generator that on-demand fetches `limit` number of items, at max `page_size` at a time.
        """
        return cls._query(auth, cls.base_url % kwargs, page_size=page_size, limit=limit, reverse=reverse)
