import json
import re
import requests

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def convert_from_camel_case(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def economic_request(auth, url, limit=1000, skip_pages=0):
    url = u"%s?pagesize=%s&skippages=%s" % (url, limit, skip_pages)
    r = requests.get(
        url,
        data=json.dumps({}),
        headers={'content-type': 'application/json', 'appId': auth.app_id, 'accessId': auth.token}
    )
    assert r.status_code == 200, "Unexpected response: %s" % r.content
    return json.loads(r.content)