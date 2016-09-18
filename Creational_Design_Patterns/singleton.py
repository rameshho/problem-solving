'''
An object oriented way of providing global variables is through singleton
Singleton is the pattern you need when you'd like to allow only one object to be instantiated from a class
There are many ways to create a singleton class
But now we are using Borg design pattern to implement our Singleton
'''

class Borg:
    """Borg class making class attributes global"""
    _shared_state = {} #Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state #Make it an attribute dictionary
        self.A = 10 + len(self.__dict__)
        self.B = 20 + len(self.__dict__)

class singleton(Borg): #Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    #This essentially makes the singletom objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)
#Let's create a singleton object and add our first acronym
x = singleton(HTTP = "Hyper Text Transfer Protocol")
# Print the object
print(x)

#Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
x1 = singleton(SNMP = "Simple Network Management Protocol")

#Print the object
print(x)
