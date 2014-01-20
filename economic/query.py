from economic.utils import economic_request


class QueryMixin(object):
    @classmethod
    def all(cls, auth, limit=1000):
        """
        Returns a generator that on-demand fetches all items, at max `limit` at a time.
        """
        assert limit <= 1000, "Max 1000 items per page allowed. The generator will automatically fetch extra pages."
        r = lambda r: economic_request(auth, cls.base_url, limit=limit, skip_pages=r)
        page = 0
        results = 1
        while page < results:
            request = r(page)
            for itm in request['collection']:
                yield cls(auth, itm)
            results = request['pagination']['results'] / limit  # Calculate number of pages
            page = request['pagination']['skipPages'] + 1