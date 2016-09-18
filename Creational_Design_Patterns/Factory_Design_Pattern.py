class Dog:
    """A simple dob class"""
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "boof!"

class Cat:
    """A simple cat class"""
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "Meow!"

def get_pet(pet='dog'):
    """The factory method"""
    pets = dict(dog=Dog("doggy"), cat = Cat("Catty"))
    return pets[pet]

my_pet = get_pet('cat')
print(my_pet.speak())

my_pet = get_pet('dog')
print(my_pet.speak())
