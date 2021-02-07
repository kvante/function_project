# list_a = [i for i in range(5)]
# print(list_a)


# list_a = ['hi','lo']
#
# list_b = [i for i in list_a[::-1]]
# print(list_b)

#list_a = [name for name in names if 'a' in name]


# list_car = [
#     {'sn': 1234,
#      'year': 1985},
#     {'sn': 4321,
#      'year': 2000},
#     {'sn': 7894,
#      'year': 2001}
# ]
#
# n = 2000
#
# list_a = [year for year in list_car for k, v in list_car.items() if v > n]
# print(list_a)

# from random import randint
# n = 3
# matrix = [[randint(1, 6) for j in range(n)] for i in range(n)]
# print(matrix)

# new_dict = {value: key for key, value in old_dict.items()}
# print(new_dict)
#
# def main ():
#     pass
#
# if __name__ == '__main__':
#     main()
#



# from collections import Counter
#
# def count(f,s):
#     if s == None:
#        return 0
#     return Counter(s).get(f)
#
list_a = [1, 3, 5, 7, 54, 3, 5, 3, 7, 5, 3, 7, 2, 45, 54, 34, 3, 6, 3, 6, 8, 5, 3]
#
#
# def count(str, item):
#     count = 0
#     for character in list(str):
#         if character == item:
#             count += 1
#     return count
# print(count(list_a))

# def lambda(name):
#     print(f'Hello,{name}')
#
# lambda()
name  = ['a','s','d','f','g','h','j']

hello_name = lambda name1: [f'Hello{i}' for i in name1]
print(hello_name(name))

name2 = ['qwer', 'lea', 'amir']
#
# hello_name = lambda name: [f'Hello {i}' for i in name]
#
# print(hello_name(name2))

# list = [lambda x:x*i for i in range(5)]
#
# print(list)
# result = map(lambda x: str(x), list_a)# vmesto cicla
#
# print(list(result))

list_b = ['kolya', 'dima']

result = filter(lambda x: 'k' in x, list_b) # otfiltrovyvaet
#name for name in names if 'a' in name
print(list(result))

from functools import reduce

items = [1,2,3,4,5,3,3]
#a = filter(lambda x: x % 3 == 0, items)
sum_all = reduce(lambda x, y: x + y, list(filter(lambda x: x % 3 == 0, items)))
print(sum_all)