import ctypes

from common import *
from int import *

def boolData(obj):
    return intData(obj)

def boolDataFromAddress(address):
    return intDataFromAddress(address)

if __name__ == '__main__':
    print("True")
    pretty_print(boolData(True))
    print("---------")
    print("False")
    pretty_print(boolData(False))
