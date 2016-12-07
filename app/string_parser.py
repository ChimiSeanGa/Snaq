import re

from .config import DESC_FMT_STRING

"""returns a dict containing:
- item
- price
- location (optional)
- description (can be empty)"""
def parse_sale(desc):
    matched = re.match(DESC_FMT_STRING, desc)
    if matched:
        return matched.groupdict()
    else:
        return None
