from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class Customer(EconomicSerializer, QueryMixin):
    id_property_name = 'customer_number'
    base_url = "https://restapi.e-conomic.com/customers/"
