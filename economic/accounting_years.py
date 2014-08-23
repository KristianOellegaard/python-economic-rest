from economic.account_entries import AccountEntry
from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class AccountingYear(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/accounting-years/"

    def __unicode__(self):
        return u"Accounting year %s:" % self.year

    def is_closed(self):
        if 'closed' in self.valid_fields:
            if self.closed:
                return True
        return False

    def get_account_entries(self):
        return AccountEntry.filter(self.auth, year=self.year)