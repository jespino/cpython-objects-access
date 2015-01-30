import ctypes

from common import *

def bytearrayData(obj):
    return bytearrayDataFromAddress(id(obj))

def bytearrayDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_size'] = ctypes.c_long.from_address(address + longsize * 2)
    common['ob_alloc'] = ctypes.c_long.from_address(address + longsize * 3)
    common['*ob_bytes'] = ctypes.c_long.from_address(address + longsize * 4)
    common['*ob_start'] = ctypes.c_long.from_address(address + longsize * 5)
    common['ob_exports'] = ctypes.c_int.from_address(address + longsize * 6)

    common['ob_bytes'] = []
    for x in range(common['ob_alloc'].value):
        common['ob_bytes'].append(ctypes.c_char.from_address(common['*ob_bytes'].value + (x * charsize)))

    common['value'] = []
    for x in range(common['ob_size'].value):
        common['value'].append(ctypes.c_char.from_address(common['*ob_start'].value + (x * charsize)))
    return common

if __name__ == '__main__':
    print("Bytearray yep")
    x = bytearray(b"yep")
    pretty_print(bytearrayData(x))
