# Access Speicifiers
# name   → Public
# _name  → Protected convention
# __name → Private through name mangling (not strict privacy)

# Variables:
# - Class Variables : define outside the constuctor function
# - Instance Variables : define inside the constuctor function


class Student:
    std_no = 0  # class/Static variable

    # Constructor
    def __init__(self, name, age, bal):
        Student.std_no += 1
        self.name = name  # Public variable
        self._age = age  # Protected variable convention (still accessiable)
        self.__bal = bal  # Private variable

    # Instance method
    def print_detail(self):
        print("print detail ----------")
        print("Name    : ", self.name)
        print("Age     : ", self._age)
        print("Bal     : ", self.__bal)
        print("Student No : ", self.std_no)

    @staticmethod
    def add_static(a, b):
        print("Static method ----------")
        return a + b

    @classmethod
    def add_class(cls, a, b):
        print("Class method ----------")
        return a + b + cls.std_no


s1 = Student("Chandru", 22, 4000)
s2 = Student("Vicky", 22, 2000)
s3 = Student("Jazz", 24, 1000)

# Access Instance Variables
print(s1.name)
print(s1._age)
# print(s1.__bal)  # AttributeError

# Access Class Variables
print(Student.std_no)


# Access Methods
s1.print_detail()
print(Student.add_static(2, 3))
print(Student.add_class(2, 3))
