class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
        
    def altered(self):
        print "PARENT altered()"
    def override(self):
        print "PARENT override()"
class Child(Parent):
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "Child, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()


