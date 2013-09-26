python-economic-rest
====================

Easy to use and dynamic python interface to the experimental e-conomic REST api


Example
-------
```python

from economic.auth import Authentication
from economic.customers import Customer
from economic.invoices import BookedInvoice, DraftInvoice
from economic.products import Product

APP_ID = "<app id>"
ACCESS_ID = "<access id>"

auth = Authentication(APP_ID, ACCESS_ID)

print BookedInvoice.all(auth)
print DraftInvoice.all(auth)
print Customer.all(auth)
print Product.all(auth)

# or

print [c.name for c in Customer.all(auth)]
print [p.name for p in Product.all(auth)]
# ..etc..

```
