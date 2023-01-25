# Polymorphism

def m1(a, b):
    print(a + b)


def m2(a, b, c):
    print(a * b * c)


print(m1(10, 20))
print(m2(10, 20, 30))

"""OverLoading-Same Method name with different parameters(signs)
   OverRiding- Same method name and same parameters when it is present in two different classes"""


class Animal:
    speech = "Bow"
    eat = "veg"

    def voice(self):
        print("Evvery animal is speak")


class Dog(Animal):
    def voice(self):
        print("Dog speech bow bow")


class Cat(Animal):
    def voice(self):
        print("cat speech meow meow")


class Cow(Animal):
    def voice(self):
        print("cow speech cooo")


obj = Cow()
obj.voice()
obj1 = Dog()
obj1.voice()

# ABSTRACT METHODS USINF ANNOTATIONS SYMBOL IS USING '@'
from abc import ABC, abstractmethod


class Area(ABC):  # inherit the abstract class in parent class
    @abstractmethod
    def calculate_area(self):
        # print("In a calculate")
        pass

    @abstractmethod
    def calculate_circle(self):
        # print("In a circle")
        pass


class Square(Area):
    def calculate_area(self):
        print("In a calculate_area")

    def calculate_circle(self):
        pass


ob = Square()
ob.calculate_area()
n = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(len(n)):
    print(n[i] ^ l[len(n) - 1 - i], end=" ")

# shift operators
print(7 << 3)  # left shift
print(7 >> 3)  # right shift

