from economic.employees import Employee
from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class InvoiceSerializer(EconomicSerializer):
    id_property_name = 'booked_invoice_number'

    def get_our_reference(self):
        if hasattr(self, 'our_reference'):
            return [employee for employee in Employee.all(self.auth) if employee.id == self.our_reference][0]
        return None

    def save(self):
        raise NotImplementedError("Please define a run method on %s" % self.__class__.__name__)

    def delete(self):
        raise NotImplementedError("Please define a delete method on %s" % self.__class__.__name__)


class BookedInvoice(InvoiceSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/invoices/booked/"


class DraftInvoice(InvoiceSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/invoices/drafts/"
