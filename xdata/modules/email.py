import re
from .domain import run as domain_run

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def run(value):
    address = value.strip().lower()
    if not EMAIL_RE.match(address):
        return {"type": "email", "email": address, "valid_format": False}

    local, domain = address.rsplit("@", 1)
    return {
        "type": "email",
        "email": address,
        "valid_format": True,
        "local_part": local,
        "domain": domain,
        "domain_info": domain_run(domain),
    }


# Compatibility entry point used by the X-Data CLI.
def lookup(value):
    return run(value)
