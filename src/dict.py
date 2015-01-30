import ctypes

from common import *

def pretty_print_dict(dict_obj):
    for key, value in dict_obj.items():
        if key == "ma_keys":
            print("ma_keys: ")
            for key2, value2 in value.items():
                if key2 == "dk_entries":
                    print("  dk_entries: [")
                    for value3 in value2:
                        for key4, value4 in value3.items():
                            print("    {}: {}".format(key4, value4))
                        print("    ----")
                    print("  ]")
                else:
                    print("  {}: {}".format(key2, value2))
        else:
            print("{}: {}".format(key, value))


def dictData(obj):
    return dictDataFromAddress(id(obj))

def dictDataFromAddress(address):
    common = commonDataFromAddress(address)
    common['ma_used'] = ctypes.c_long.from_address(address + longsize * 2)
    common['*ma_keys'] = ctypes.c_long.from_address(address + longsize * 3)
    common['*ma_values'] = ctypes.c_long.from_address(address + longsize * 4)

    ma_keys_address = common['*ma_keys'].value
    common['ma_keys'] = OrderedDict()
    common['ma_keys']["dk_refcnt"] = ctypes.c_long.from_address(ma_keys_address)
    common['ma_keys']["dk_size"] = ctypes.c_long.from_address(ma_keys_address + longsize)
    common['ma_keys']["dk_lookup"] = ctypes.c_long.from_address(ma_keys_address + longsize * 2)
    common['ma_keys']["dk_usable"] = ctypes.c_long.from_address(ma_keys_address + longsize * 3)
    common['ma_keys']["dk_entries"] = []

    dk_entries_address = common['*ma_keys'].value + longsize * 4
    for x in range(common['ma_keys']['dk_size'].value):
        entry_address = dk_entries_address + x * longsize * 3
        common['ma_keys']['dk_entries'].append(OrderedDict([
            ("me_hash", ctypes.c_long.from_address(entry_address)),
            ("me_key", ctypes.c_long.from_address(entry_address + longsize)),
            ("me_value", ctypes.c_long.from_address(entry_address + longsize * 2)),
        ]))

    return common

if __name__ == '__main__':
    print("Dict {1: 2, 3: 4}")
    x = {1: 2, 3: 4}
    pretty_print_dict(dictData(x))
