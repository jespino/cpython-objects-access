import ctypes

from common import *

def bytesData(obj):
    return bytesDataFromAddress(id(obj))

def bytesDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_size'] = ctypes.c_long.from_address(address + longsize * 2)
    common['ob_shash'] = ctypes.c_long.from_address(address + longsize * 3)
    common['ob_sval'] = []
    for x in range(common['ob_size'].value + 1):
        common['ob_sval'].append(ctypes.c_char.from_address(address + longsize * 4 + (x * charsize)))
    return common

if __name__ == '__main__':
    print("Bytes yep")
    pretty_print(bytesData(b"yep"))
