class Parent(object):
    def override(self):
        print "I am parent"

class Child1(Parent):
    def override(self):
        print "I am Child1"

class Child2(Parent):
    def override(self):
        print "I am Child2"

class GrandChild(Child1, Child2):
    def override(self):
        print dir(self)
        print "I am GrandChild"
##       super(GrandChild, self).override()
##       super(Child1, self).override()
        super(Child2, self).override()
        print "Done"
       
GC = GrandChild()
GC.override()
