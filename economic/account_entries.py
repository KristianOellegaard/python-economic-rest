from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class AccountEntry(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/accounting-years/%(year)s/entries"  # Use .filter(year=2014)

    @classmethod
    def all(cls, auth, limit=1000):
        raise Exception("Please use .filter() and provide year as keyword argument")

    def __unicode__(self):
        return u"Account %s: Entry: %s %s %s" % (self.account['accountNumber'], self.entry_number, self.date, self.amount_in_base_currency)