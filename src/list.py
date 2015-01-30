import ctypes

from common import *

def listData(obj):
    return listDataFromAddress(id(obj))

def listDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ob_size'] = ctypes.c_long.from_address(address + longsize * 2)
    common['*ob_item'] = ctypes.c_long.from_address(address + longsize * 3)
    common['allocated'] = ctypes.c_long.from_address(address + longsize * 4)

    common['ob_item'] = []
    for x in range(common['allocated'].value):
        common['ob_item'].append(ctypes.c_long.from_address(common['*ob_item'].value + x * longsize))

    common['value'] = []
    for x in range(common['ob_size'].value):
        common['value'].append(ctypes.c_long.from_address(common['*ob_item'].value + x * longsize))
    return common

if __name__ == '__main__':
    print("List [1,2,3]")
    x = [1,2,3]
    pretty_print(listData(x))
    x.append(1)
    x.append(2)
    x.append(3)
    x.pop()
    x.pop()
    x.pop()
    print("----------")
    print("List [1,2,3] after changes")
    pretty_print(listData(x))
