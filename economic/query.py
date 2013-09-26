from economic.utils import economic_request


class QueryMixin(object):
    @classmethod
    def all(cls, auth, limit=1000):
        assert limit <= 1000, "Multi page queries not yet implemented. Reduce limit to 1000 or less"
        return [cls(auth, itm) for itm in economic_request(auth, cls.base_url)['collection']]