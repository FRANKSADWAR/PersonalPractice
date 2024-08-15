from employee import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "Orders from", server)
    def pay(self, server):
        print(self.name, "Pays for item to", server)


class Oven:
    def bake(self):
        print("Oven bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')   ## Embeded other objects in here
        self.chef = PizzaRobot('Bob')  ## a robot chef named Bob
        self.oven = Oven()              ## The oven of the pizza shop

    def order(self, name):
        customer = Customer(name)           ## Activate other objects
        customer.order(self.server)         ### Customer places an order from the server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()
    scene.order('Homer')
    print('..........')
    scene.order('Shaggy')



"""
The Pizza class is a container and a controller, its constructor makes and embeds instances of the employee classes we wrote in employee.py 
and also the oven class.
"""