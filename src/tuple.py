import ctypes

from common import *

def tupleData(obj):
    return tupleDataFromAddress(id(obj))

def tupleDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_size'] = ctypes.c_long.from_address(address + longsize * 2)
    common['ob_item'] = []
    for x in range(common['ob_size'].value):
        common['ob_item'].append(ctypes.c_long.from_address(address + longsize * 3 + x * longsize))
    return common

if __name__ == '__main__':
    print("Tuple (1,2,3)")
    x = (1,2,3)
    pretty_print(tupleData(x))
