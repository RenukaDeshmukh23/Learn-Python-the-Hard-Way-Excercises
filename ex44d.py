class Parent(object):                                                           #Class Parent is declared/defined.
    def override(self):                                                         #Override() for Parent class is defined.
        print("PARENT override() line3")                                              #print the given message.

    def implicit(self):                                                         #implicit() is defined.
        print("PARENT implicit() line6")                                              #print the given message.

    def altered(self):                                                          #altered() is defined.
        print("PARENT altered() line9")                                               #print the given message.

class Child(Parent):                                                            #Class Child is declared and Parent class is inherited.
    def override(self):                                                         #override() is defined for class Child.
        print("CHILD override() line13")                                               #print the given message

    def altered(self):                                                          #for class child altered() is declered.
        print("CHILD altered() line16")                                                #print the given message.
        super(Child,self).altered()                                             #call super with arguments child and self. and then alterd()
        print("CHILD,AFTER PARENT altered() line18")                                   #print the given message

dad = Parent()                                                                  #assign Parent to variable dad
son = Child()                                                                   #assign Child to variable child

dad.implicit()                                                                  #
son.implicit()
print("\n")

dad.override()
son.override()
print("\n")

dad.altered()
son.altered()
print("\n")
