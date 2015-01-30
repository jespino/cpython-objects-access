import ctypes

from common import *

def intData(obj):
    return intDataFromAddress(id(obj))

def intDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_size'] = ctypes.c_long.from_address(address + longsize * 2)
    common['ob_digit'] = []
    for x in range(common['ob_size'].value):
        common['ob_digit'].append(ctypes.c_int.from_address(address + longsize * 3 + (x * intsize)))
    return common

if __name__ == '__main__':
    print("Number 10")
    pretty_print(intData(10))
    print("---------")
    print("Number {}".format(1024**3+100))
    pretty_print(intData(1024**3+100))
