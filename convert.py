import json
import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

domains = []
for line in lines:
    if line.startswith("server="):
        domain = line.split("/")[1]
        domains.append(domain)

source = {"version": 1, "rules": [{"domain_suffix": domains}]}

with open(sys.argv[2], "w") as f:
    json.dump(source, f, indent=2)
