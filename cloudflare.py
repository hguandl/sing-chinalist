import json

import requests

result = requests.get("https://api.cloudflare.com/client/v4/ips").json()["result"]

ips = result["ipv4_cidrs"] + result["ipv6_cidrs"]

source = {"version": 1, "rules": [{"ip_cidr": ips}]}

with open("geoip-cloudflare.json", "w") as f:
    json.dump(source, f, indent=2)
