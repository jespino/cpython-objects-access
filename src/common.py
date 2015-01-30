import ctypes
from collections import OrderedDict

longsize = ctypes.sizeof(ctypes.c_long)
doublesize = ctypes.sizeof(ctypes.c_double)
intsize = ctypes.sizeof(ctypes.c_int)
charsize = ctypes.sizeof(ctypes.c_char)

def pretty_print(data_dict):
    for (key, value) in data_dict.items():
        print("{}: {}".format(key, value))

def commonDataFromAddress(address):
    ob_refcnt = ctypes.c_long.from_address(address)
    ob_type = ctypes.c_long.from_address(address + longsize)

    return OrderedDict([
        ("id", address),
        ("ob_refcnt", ob_refcnt),
        ("ob_type", ob_type),
    ])

def commonData(obj):
    return commonDataFromAddress(id(obj))
