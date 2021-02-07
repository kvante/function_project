# def my_decorator(func):
#    def do_some_staff():
#        print('heloword')
#        result = func()
#        print('heloword')
#        return result
#    return do_some_staff
#
#
# @my_decorator
# def my_func():
#     print('hi')
#
#
# my_func()

# from datetime import datetime
#
# time = datetime.now()
#
# def my_time(func):
#     def print_time():
#         print(time)
#     return print_time()
#
#
# @my_time
# def time_func():
#     pass



# def my_decorator(func):
#     def return_a():
#         a = func()
#         b = [i for i in a if i % 2 == 0]
#         print(b)
#
#     return return_a()
#
# @my_decorator
# def listb():
#     a = list(range(1,9))
#     return a




# def my_decorator(func):
#     def do_smth():
#         list = func()
#         new_list = [i for i in list if i % 2 == 0]
#         print(new_list)
#         return func(), new_list
#     return do_smth()
#
#
# @my_decorator
# def myfunc():
#     list = [i for i in range(1, 11, 1)]
#     return list

# my_file = open('text.txt')
# print(my_file.readline())
# my_file.close()
# while True:
#     line = [my_file.readline()]
#     a = 0
#     for i in line:
#         a += 1
#     if a == 5:
#         print(line)
#
#     if not line:
#         break

# print(my_file.readlines())

# with open('text.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)

# with open('text.txt','a') as my_file:
# #     a = 1
# #     while a < 4:
# #         a += 1
# #         my_file.write(input('str:  ') + '\n'

with open('text.txt') as source, open('text1.txt', 'w') as destination:
    for line in source:
        line = line.replace('0', '1')
        destination.write(line)
#
# with open('text.txt') as my_file:
#     new_list = [i for i in i if i % 2 == 0]



