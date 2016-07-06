from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class AccountEntry(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/accounting-years/%(year)s/entries"  # Use .filter(year=2014)

    @classmethod
    def all(cls, auth, limit=None, page_size=1000):
        raise Exception("Please use .filter() and provide year as a keyword argument")

    @classmethod
    def filter(cls, auth, year=None, **kwargs):
        if not year:
            raise Exception("Please provide a year argument to .filter()")
        base_url = cls.base_url % {'year': year}
        return super(AccountEntry, cls).filter(auth, base_url=base_url, **kwargs)

    def __unicode__(self):
        return u"Account %s: Entry: %s %s %s" % (self.account['accountNumber'], self.entry_number, self.date, self.amount_in_base_currency)
