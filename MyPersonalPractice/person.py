import math

class Person:
    def __init__(self, name, job = None, pay = 0, tax = 0):
        ## the data to be attached to the instance is passed as arguments to the constructor method and assigned to self
        self.name = name
        self.job = job
        self.pay = pay
        self.tax = tax

    def __str__(self): ## print the object with operator overloading method
        return '[%s : %s]' % (self.__class__.__name__, self.__dict__)

    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        if self.tax:
            self.pay = int(self.pay * (1 + percent))
            self.pay = self.pay * (1 - self.tax)
        else:
            self.pay = int(self.pay * (1 + percent))

        

class Manager(Person):  ## Manager inherits the superclass Person
    ## we can also customize the constructor too
    def __init__(self, name, pay,tax =0):
        Person.__init__(self, name, 'Manager', pay, tax) ## run the original with Mgr defined by default
        
    ## we will augment the original method instead of replacing it all together, this is a good practice for code maintenance
    def giveRaise(self, percent, bonus = 0.10):
        Person.giveRaise(self, percent + bonus)    ### we have simply augmented the original method here instead of coding it afresh

        
if __name__ == "__main__":
    ## self test code
    will = Person('Will Morgan', job = 'GIS Developer', pay = 100000)
    sue = Person('Sue Jones', job='AI Engineer', pay = 100000)
    seb = Manager('Sebastian', 120000, 0.2)
    print(seb)

    jon = Person('John Doe')

    print("\n=== All three of them ====\n")
    for object in (sue, will, seb, jon):
        object.giveRaise(0.10)
        print(object)



