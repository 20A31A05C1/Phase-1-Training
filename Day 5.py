# Inheritance

# Single
class Parent:
    @staticmethod
    def func1():
        print("This function is in parent class.")


class Child(Parent):
    @staticmethod
    def func2():
        print("This function is in child class.")


object = Child()
object.func1()
object.func2()


# Hierarchical

class Parent:
    @staticmethod
    def func1():
        print("This function is in parent class.")


class Child1(Parent):
    @staticmethod
    def func2():
        print("This function is in child 1.")


class Child2(Parent):
    @staticmethod
    def func3():
        print("This function is in child 2.")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# Multiple

class Mother:
    mother_name = ""

    def mother(self):
        print(self.mother_name)


class Father:
    father_name = ""

    def father(self):
        print(self.father_name)


class Son(Mother, Father):
    def parents(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


s1 = Son()
s1.father_name = "RAM"
s1.mother_name = "SITA"
s1.parents()
