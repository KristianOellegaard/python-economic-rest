from economic.utils import economic_request


class QueryMixin(object):
    @classmethod
    def _query(cls, auth, base_url, page_size, limit=None):
        assert page_size <= 1000, "Max 1000 items per page allowed. The generator will automatically fetch extra pages."
        page = 0
        total_pages = (limit/page_size) if limit and page_size else 1
        while page <= total_pages:
            request = economic_request(auth, base_url, limit=page_size, skip_pages=page)
            for itm in request['collection']:
                yield cls(auth, itm)
            if not limit:
                total_pages = request['pagination']['results'] / page_size  # Calculate number of pages
            page += 1

    @classmethod
    def all(cls, auth, page_size=1000, limit=None):
        """
        Returns a generator that on-demand fetches all items, at max `limit` at a time.
        """
        return cls._query(auth, cls.base_url, page_size=limit)

    @classmethod
    def filter(cls, auth, page_size=1000, limit=None, **kwargs):
        """
        Returns a generator that on-demand fetches all items, at max `limit` at a time.
        """
        return cls._query(auth, cls.base_url % kwargs, page_size=limit)
