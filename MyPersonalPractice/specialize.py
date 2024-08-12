from abc import ABCMeta, abstractmethod

"""
    -Class interface techniques 

    Super:Defines a method function and a delegate that expects an action in a subclass
    Inheritor: Doesn't provide any new names, so it gets everything defined in Super
    Replacer: Override's Super's method with a version of its own
    Extender: Customizes Super's method by overriding and calling back to run the default.
    Provider: Implements the action method expected by Super's delegate method
"""

class Super:
    def method(self):
        print('in Super.method')  ## this is the default behavior
    def delegate(self):
        self.action()            ## expected to be defined, this is an abstract superclass because it expects some of its methods to be defined by a subclass. Super is called an Abstract superclass

class Inheritor(Super):           ## Inherits Super verbatim
    pass    

class Replacer(Super):
    def method(self):
        print("in Replacer.method")
    

class Extender(Super):
    def method(self):
        print("starting Extender.method")
        Super.method(self) ## calling the default action from the superclass
        print("Ending Extender.method")

class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print("\n" + klass.__name__ + "...")
        klass().method()

    x = Provider()
    x.delegate()