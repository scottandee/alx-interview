#!/usr/bin/python3
"""utf8 Validation
"""


def validUTF8(data):
    """This script determines if a given set of
    data is valid utf8
    """
    for d in data:
        if isinstance(type(d), int):
            return False
        if d >= 256:
            return False
    return True
