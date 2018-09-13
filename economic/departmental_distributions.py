from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class DepartmentalDistributions(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/departmental-distributions/"
