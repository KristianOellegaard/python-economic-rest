from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class Employee(EconomicSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/employees/"

    def __unicode__(self):
        return self.name
