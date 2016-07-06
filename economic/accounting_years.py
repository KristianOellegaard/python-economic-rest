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

    def get_account_entries(self, limit=None):
        # self.entries is the URL for this AccountingYear's entries
        # we have to remove the query parameters from the URL first, since they are added again by _query
        return AccountEntry._query(self.auth, self.entries.split('?')[0], limit=limit)
