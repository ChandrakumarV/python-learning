# 1. Single Inheritance
# One child class inherits from one parent class.


class Parent:
    def display(self):
        print("Parent class")


class Child(Parent):
    def show(self):
        print("Child class")


obj = Child()
obj.display()
obj.show()


# 2. Multilevel Inheritance
# A child class inherits from a parent, and another class inherits from that child.


class Grandparent:
    def grand(self):
        print("Grandparent")


class Parent(Grandparent):
    def parent(self):
        print("Parent")


class Child(Parent):
    def child(self):
        print("Child")


obj = Child()
obj.grand()
obj.parent()
obj.child()

# 3. Multiple Inheritance
# One child class inherits from multiple parent classes.


class Father:
    def father(self):
        print("Father")


class Mother:
    def mother(self):
        print("Mother")


class Child(Father, Mother):
    def child(self):
        print("Child")


obj = Child()
obj.father()
obj.mother()
obj.child()

# 4. Hierarchical Inheritance
# Multiple child classes inherit from the same parent class.


class Parent:
    def display(self):
        print("Parent")


class Child1(Parent):
    def show1(self):
        print("Child 1")


class Child2(Parent):
    def show2(self):
        print("Child 2")


obj1 = Child1()
obj1.display()
obj1.show1()

obj2 = Child2()
obj2.display()
obj2.show2()

# 5. Hybrid Inheritance
# A combination of two or more types of inheritance.


class A:
    def show_a(self):
        print("Class A")


class B(A):
    def show_b(self):
        print("Class B")


class C(A):
    def show_c(self):
        print("Class C")


class D(B, C):
    def show_d(self):
        print("Class D")


obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()


## Quick revision

# | Type         | Meaning                          |
# | ------------ | -------------------------------- |
# | Single       | One parent → One child           |
# | Multilevel   | Grandparent → Parent → Child     |
# | Multiple     | Multiple parents → One child     |
# | Hierarchical | One parent → Multiple children   |
# | Hybrid       | Combination of inheritance types |
