#
# class Foo:
#     def __init__(self, name):
#         self.name = name
#         self.__name_uppercase = name.upper()
#
#     def _method(self):
#         pass
#
# #########################################
#
# foo1 = Foo('Hello')
# print(foo1._Foo__name_uppercase)


# def _foo():
#     print('_foo')
#
#
def bar():
    a = 1
    _foo()

# import sys
from sys import *

path = 'ADWAWD'
print(globals())
print(path)
