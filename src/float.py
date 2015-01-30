import ctypes

from common import *

def floatData(obj):
    return floatDataFromAddress(id(obj))

def floatDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_fval'] = ctypes.c_double.from_address(address + longsize * 2)
    return common

if __name__ == '__main__':
    print("Number 1.5")
    pretty_print(floatData(1.5))
