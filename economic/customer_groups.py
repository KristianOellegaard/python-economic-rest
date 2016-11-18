from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class CustomerGroup(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/customer-groups/"
