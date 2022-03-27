a = 1

def foo():
    a = 2
    # print(f'In foo locals are {locals()}')
    print(f'In foo var a is {a}')
    def bar():
        # a = 3
        print(f'In bar a is {a}')
    bar()

foo()
# print(f'locals are {locals()}')
# print(f'Globals are {globals()}')
# print(f'Global a is {a}')

'''
L - local
E - enclosing
G - global
B - builtins
'''
