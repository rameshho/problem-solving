class Dog:
    """One of the objects to be returned"""
    def speak(self):
        return "Boof!"
    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Returns a dog object"""
        return Dog()
    def get_food(self):
        """Return a Dog food"""
        return "Dog Food!"

class PetStore:
    """PetStore house are Abstract Factory"""
    def __init__(self, pet_factory=None):
        """Pet factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is `{}`!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

#Create a Concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()
