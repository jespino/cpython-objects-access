import ctypes

from common import *

def complexData(obj):
    return complexDataFromAddress(id(obj))

def complexDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_cval.real'] = ctypes.c_double.from_address(address + longsize * 2)
    common['ob_cval.imag'] = ctypes.c_double.from_address(address + longsize * 2 + doublesize)
    return common

if __name__ == '__main__':
    print("Number 3 + 2j")
    pretty_print(complexData(3 + 2j))
