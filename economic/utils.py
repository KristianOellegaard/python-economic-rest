import json
import re
import requests

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def convert_from_camelCase(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def economic_request(auth, url):
    r = requests.get(url,
                     data=json.dumps({}),
                     headers={'content-type': 'application/json', 'appId': auth.app_id, 'accessId': auth.token}
    )
    return json.loads(r.content)