from copy import deepcopy, copy

lst1 = [1, 2, 3, [4, 5]]
# lst2 = lst1.copy()
lst2 = deepcopy(lst1)

lst1[-1].append(6)
print(lst1)
print(lst2)
# print(id(lst1))
# print(id(lst2))
# print(lst1 is lst2)


[1, 2, 3]  # copy
[1, 2, 3, [4, 5], {1: 2}]  # deepcopy
