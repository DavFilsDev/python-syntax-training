# CONSTRUCTORS IN PYTHON

# The __init__ method is a special method used to initialize an object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating a student
s1 = Student("Alice", 20)
s1.info()

# MEMO:
# - __init__ is automatically called when an object is created.
# - self refers to the current instance of the class.
