from abc import ABCMeta, abstractmethod

class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return "<Employee: name =%s, salary=%s>" % (self.name, self.salary)
    
    def getSalary(self):
        print("Employee salary ===>", '$' + str(self.salary))
        
class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "Maked Food")

class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 40000)
    
    def work(self):
        print(self.name, "Interfaces with customers")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "Makes pizzas all day long")

if __name__ == "__main__":
    bob = PizzaRobot('Bob')
    print(bob)
    print("Robot Salary ==>", bob.salary)
    bob.work()
    server1 = Server("Greer")
    print(server1)
    server1.giveRaise(0.15)
    server1.getSalary()

    for klass in (Employee, Chef, Server, PizzaRobot):
        obj = klass(klass.__name__)
        obj.work()

    