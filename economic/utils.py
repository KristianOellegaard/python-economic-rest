import json
import re
import requests

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def convert_from_camel_case(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


class EconomicAPIException(Exception):
    pass


class PermissionDenied(EconomicAPIException):
    pass


class ResourceDoesNotExist(EconomicAPIException):
    pass

def economic_request(auth, url, limit=1000, skip_pages=0):
    url = u"%s?pagesize=%s&skippages=%s" % (url, limit, skip_pages)
    r = requests.get(
        url,
        data=json.dumps({}),
        headers={'content-type': 'application/json', 'appId': auth.app_id, 'accessId': auth.token}
    )
    if r.status_code == 200:
        return json.loads(r.content)
    elif r.status_code == 401:
        raise PermissionDenied()
    elif r.status_code == 404:
        raise ResourceDoesNotExist()
    else:
        raise EconomicAPIException(r.content)