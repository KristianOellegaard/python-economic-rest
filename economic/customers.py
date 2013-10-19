from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class Customer(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/customers/"
