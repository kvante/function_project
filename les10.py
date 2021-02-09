#
# class Dog:
#     pass
#
# dog = Dog()
# ddd = Dog()
#
# print(Dog())

# class Dog:
#     def bark(self):
#         print('woof woof!')
#
#     def jump(self):
#         print('Jump')
#
#     def run(self):
#         print('Run')
#
#
#
# dog1 = Dog()
# dog1.jump()
# dog1.run()
# dog1.bark()

# class Dog:
#     def __init__(self, name):
#         self.name = name
#
# dog1 = Dog('charley')
# dog2 = Dog('bob')
#
# print(dog1.name,dog2.name)

# class Dog:
#     def __init__(self, height,weight,name,age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print('woof woof!')
#
#     def jump(self):
#         print('Jump')
#
#     def run(self):
#         print('Run')
#
#     def change_height(self,height):
#         self.height = height
#
#     def change_name(self,name):
#         self.name = name
#
# dog = Dog(5,12,'bob',8)
# dog.jump()
# dog.run()
# dog.bark()
#
# print(dog.name, dog.height, dog.age, dog.weight)
# dog.change_height(20)
# print(dog.height)
#
# dog.change_name('sharik')
# print(dog.name)



# class Dog:
#     def __init__(self, name, age, weight,master):
#         self.__name = name
#         self._age = age
#         self.weight = weight
#         self.__master = master
#
#     def get_master(self):
#
#         return self.__master
#
#     def set_master(self):
#         self.__master = master
#
#
#
#
# dog = Dog('bob',8,2.4,'ww')
# #print(dog.__name)
# print(dog._Dog__name)
# print(dog._age)
# print(dog.weight)
# class Dog:
#     def __init__(self):
#         self.__adress = 'minsk'
#     def get_adress(self):
#         return self.__adress
#     def set_adress(self,adress):
#         self.__adress = adress
#
# dog = Dog()
#
# print(dog.get_adress())
# dog.set_adress('prague')
# print(dog.get_adress())

# class Dog:
#     def __init__(self, master,age,name):
#         self.__master = master
#         self.__age = age
#         self.__name = name
#     @property
#     def master(self):
#         return self.__master
#
#     @master.setter
#     def master(self, master):
#         if len(master) < 5:
#             self.__master = master
#
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name





# dog = Dog('Alex', 12,22)
# dog.master = 'Moe'
# print(dog.master)
# dog.age = 13
# print(dog.age)
# dog.name = 3
# print(dog.name)

class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self, age):
        self.birthday = age + 1

    def sleep(self):
        print('11')

    def bark(self):
        print('woof')


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self, age):
        self.birthday = age + 1

    def sleep(self):
        print('11')

    def meow(self):
        print('meow')


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('run')

    def jump(self):
        print('jump')

    def birthday(self, age):
        self.birthday = age + 1

    def sleep(self):
        print('11')

    def fly(self):
        print('uu')

class Parrent:
    def print_world(self):
        print('world')
class Child(Parrent):
    def print_hello(self):
        print('Hello')

class Pet(Dog,Cat, Parrot):





