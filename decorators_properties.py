class Person(object):               #this mechanism is present in object
    counter = 0
    def __init__(self, name, age):
        self.name = name             #it will invoke setter decorative of name
        self.age = age               #it will invoke setter decorative of age
        Person.counter += 1

    @staticmethod                    #This method is used to create static attribute
    def count():
        return Person.counter

    @property                         #reading the attribute name
    def name(self):
        return self._name

    @property                          #reading the attribute age
    def age(self):
        return self._age   #it will recursively call read function property if we use self.age to overcome from it we need to use self._age to set the attribute

    @name.setter                          #setting the attribute name
    def name(self, name ):
        print "i am here"
        self._name = name

    @age.setter                         #setting the attribute age
    def age(self, age):
        if age > 100:
            pass
        else:
            self._age = age

p = Person("hosamani", 20)
p.name = "ramesh"                     #it will invoke a setter decorative name
print p.name                          #it will invoke reading decorative name

p.age = 100                          #it will invoke a setter decorative age
print p.age                          #it will invoke reading decorative of age
p1 = Person( "sharan", 26 )
print "Number of objects created of class Person = ", Person.counter                 #Used to retrieve number of objects created

#Important note :- Getter(i.e property) should come first before setter
#The set decorative main purpose of usage is asign a value to attribute after doing validation
#syntax will also become easy using decoratives and properties
