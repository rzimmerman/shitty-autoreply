import os
from bisect import bisect


# Cache the names list
_NAMES = None


def load_names():
    """Load the names.txt file into memory"""
    global _NAMES
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'names.txt')) as f:
        _NAMES = sorted(name.strip().upper() for name in f.readlines())
    return _NAMES


def wrong_name(name):
    """Return a name that is slightly different from name"""
    if _NAMES is None:
        load_names()
    uname = name.upper()
    i = bisect(_NAMES, uname)
    if i >= len(_NAMES) - 1:
        opt_a = _NAMES[-1]
        opt_b = _NAMES[-2]
    elif i == 0:
        opt_a = _NAMES[0]
        opt_b = _NAMES[1]
    else:
        opt_a = _NAMES[i-1]
        opt_b = _NAMES[i+1]
    if opt_a == uname:
        return opt_b.capitalize()
    elif opt_b == uname:
        return opt_a.capitalize()
    else:
        name_val = sum(ord(c) for c in uname)
        return max(
            opt_a, opt_b,
            key=lambda o: sum(ord(c) for c in o) - name_val).capitalize()
