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


def economic_request(auth, url, request_params=None, timeout=60):
    if not request_params:
        request_params = {}
    url = u'%s?%s' % (url, u'&'.join([u'%s=%s' % (field, value) for field, value in request_params.items()]))
    r = requests.get(
        url,
        headers={'content-type': 'application/json', 'appId': auth.app_id, 'accessId': auth.token},
        timeout=timeout
    )
    if r.status_code == 200:
        return json.loads(r.content)
    elif r.status_code == 401 or r.status_code == 403:
        raise PermissionDenied()
    elif r.status_code == 404:
        raise ResourceDoesNotExist()
    else:
        raise EconomicAPIException(r.content)
