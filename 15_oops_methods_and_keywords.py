# 1. Method Overriding
# Child class defines its own version of the parent method.


class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):  # Overrides the parent method
        print("Child method")


obj = Child()
obj.show()  # Output: Child method


# 2. Overwriting
# Assigning a new value to an existing variable or attribute.


class Parent:
    name = "Parent"


class Child(Parent):
    name = "Child"  # Redefines the inherited class attribute


obj = Child()
print(obj.name)  # Output: Child


# 3. pass Keyword
# pass does nothing. It is used as a placeholder for future code.


class Student:
    pass  # Empty class


class Teacher:
    def show(self):
        pass  # Empty method


obj = Student()
print("Student object created")


# 4. super() Keyword
# super() calls methods from the parent class.
# It is commonly used to call the parent constructor.


class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls the parent constructor
        self.age = age


obj = Child("Ravi", 21)
print(obj.name)  # Output: Ravi
print(obj.age)  # Output: 21


# 5. Method Overloading
# Python does not support traditional method overloading directly.
# Default arguments can be used to handle different numbers of arguments.


class Calculator:
    def add(self, a, b=0):
        return a + b


obj = Calculator()
print(obj.add(10))  # Output: 10
print(obj.add(10, 20))  # Output: 30


# 6. Constructor Overriding
# Child class defines its own __init__() constructor.
# The parent constructor is not called automatically.


class Parent:
    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    def __init__(self):
        print("Child constructor")


obj = Child()  # Output: Child constructor
