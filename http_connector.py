import requests
from logger import Logger


l = Logger(__name__)

def Get(uri, auth, parse=None):
    r = requests.get(uri, auth=auth)
    l.debug("GET {} RECV: (HTTP {}, {} bytes).".format(uri, r.status_code, len(r.content)))
    if not parse:
        return r.text
    elif parse == "common":
        return ParseCommon(r.text)
    elif parse == "XML":
        raise Exception("Unimplemented")
    elif parse == "blob":
        return r.content
    else:
        raise Exception("Unknown response type.")

def ParseCommon(buf):
    parsed = {}
    for l in buf.splitlines():
        try:
            var, val = l.split('=')
            parsed[var] = val
        except ValueError:
            pass
    return parsed
