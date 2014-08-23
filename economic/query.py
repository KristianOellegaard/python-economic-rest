from economic.utils import economic_request


class QueryMixin(object):
    @classmethod
    def _query(cls, auth, base_url, page_size):
        assert page_size <= 1000, "Max 1000 items per page allowed. The generator will automatically fetch extra pages."
        r = lambda r: economic_request(auth, base_url, limit=page_size, skip_pages=r)
        page = 0
        results = 1
        while page < results:
            request = r(page)
            for itm in request['collection']:
                yield cls(auth, itm)
            results = request['pagination']['results'] / page_size  # Calculate number of pages
            page = request['pagination']['skipPages'] + 1

    @classmethod
    def all(cls, auth, limit=1000):
        """
        Returns a generator that on-demand fetches all items, at max `limit` at a time.
        """
        return cls._query(auth, cls.base_url, page_size=limit)

    @classmethod
    def filter(cls, auth, limit=1000, **kwargs):
        """
        Returns a generator that on-demand fetches all items, at max `limit` at a time.
        """
        return cls._query(auth, cls.base_url % kwargs, page_size=limit)
