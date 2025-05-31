# INHERITANCE IN PYTHON

# Inheritance allows one class to inherit properties and methods from another.

class Animal:
    def speak(self):
        print("Some animal sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()  # Inherited method
d.bark()   # Own method

# MEMO:
# - ChildClass(ParentClass) defines inheritance.
# - Inherited methods can be overridden.
