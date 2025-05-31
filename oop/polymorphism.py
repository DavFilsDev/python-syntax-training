# POLYMORPHISM IN PYTHON

# Polymorphism allows objects of different classes to be treated as the same interface.

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

def make_sound(animal):
    animal.sound()

c = Cat()
w = Cow()

make_sound(c)
make_sound(w)

# MEMO:
# - Different classes can implement the same method.
# - The same function can operate on different types.
