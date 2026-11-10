
# ------------------------------------------------------------
# OBJECT-ORIENTED PROGRAMMING (OOP)
# ------------------------------------------------------------

# Class: Blueprint for creating objects.
# Object: Instance of a class.

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def display(self):
        print(self.name, self.age)


# Creating objects
s1 = Student("Shivang", 18)
s2 = Student("Rahul", 19)

s1.display()
s2.display()


# INHERITANCE

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()
d.sound()
d.bark()


# POLYMORPHISM

class Cat:

    def sound(self):
        print("Meow")


class Cow:

    def sound(self):
        print("Moo")


for animal in [Cat(), Cow()]:
    animal.sound()


# ENCAPSULATION

class Bank:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance


account = Bank()
print(account.get_balance())

