python-economic-rest
====================

Easy to use and dynamic python interface to the experimental e-conomic REST api


Basic example
-------------
```python

from economic.auth import Authentication
from economic.customers import Customer
from economic.invoices import BookedInvoice, DraftInvoice
from economic.products import Product

APP_ID = "<app id>"
ACCESS_ID = "<access id>"

auth = Authentication(APP_ID, ACCESS_ID)

print list(BookedInvoice.all(auth))
print list(DraftInvoice.all(auth))
print list(Customer.all(auth))
print list(Product.all(auth))
print list(Product.all(auth))

# or

print [c.name for c in Customer.all(auth)]
['Acme']
print [p.name for p in Product.all(auth)]
['Do-It-Yourself Tornado Kit']
# ..etc..

# Find usable fields

print list(BookedInvoice.all(auth))[0].valid_fields
[u'customer_city', u'customer_name', u'gross_amount', u'currency', u'vat_amount', u'customer_country', u'net_amount', u'id', u'layout_id', u'net_amount_base_currency', u'due_date', u'is_vat_included', u'rounding_amount', u'order_id', u'customer_address', u'sales_document_type', u'date', u'deduction_amount', u'remainder', u'term_of_payment_id', u'remainder_base_currency', u'customer_postal_code', u'pdf', u'customer', u'self']
# Beware that economic might not always give us all the fields, so this could vary slightly per invoice

```


Filtering
---------

You can filter on any field and using any of the supported operators. 
See https://restdocs.e-conomic.com/#filtering

Currently, only the AND logical operator is supported.


```python
from economic.auth import Authentication
from economic.invoices import BookedInvoice

auth = Authentication('demo', 'demo')
print list(BookedInvoice.filter(auth, currency='USD', date__gte='2012-01-01'))
```

