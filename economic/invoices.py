from economic.query import QueryMixin
from economic.serializer import EconomicSerializer
from economic.utils import convert_from_camelCase


class InvoiceSerializer(EconomicSerializer):
    @property
    def customer(self):
        # Use self.customer_url to fetch the customer
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError("Please define a run method on %s" % self.__class__.__name__)

    def delete(self):
        raise NotImplementedError("Please define a delete method on %s" % self.__class__.__name__)


class BookedInvoice(InvoiceSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/invoices/booked/"


class DraftInvoice(InvoiceSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/invoices/drafts/"