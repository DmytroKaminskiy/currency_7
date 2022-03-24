# callable

# getattr, setattr, delattr, hasattr

# class Human:
#     pass
    # def __init__(self, first_name):
    #     self.first_name = first_name


# h1 = Human()
# # h1.first_name = 'Dima'
#
# attr_names = {
#     'first_name': 'Dima',
#     'last_name': 'Kaminskyi',
#     'age': 30,
# }
# for attr_name, attr_value in attr_names.items():
#     setattr(h1, attr_name, attr_value)
#
# # print(h1.first_name)
# if hasattr(h1, 'first_name'):
#     delattr(h1, 'first_name')
# print(getattr(h1, 'first_name', 'NO ATTR'))

# class Human:
#
#     @property
#     def full_name(self):
#         pass


def foo():
    print('FOO')

print(callable(foo))


class Human:

    def __init__(self, first_name):
        self.first_name = first_name

    def foo(self):
        print('Call.foo')

h1 = Human('Dima')
# attr_name = 'first_name'
attr_name = 'foo'

if hasattr(h1, attr_name):
    attr = getattr(h1, attr_name)
    if callable(attr):
        print(attr())
    else:
        print(attr)
