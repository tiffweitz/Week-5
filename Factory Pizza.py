from abc import ABCMeta, abstractmethod
class Pizza(metaclass = ABCMeta):
    def __init__(self, toppings = "None"):
        self.toppings = toppings
    @abstractmethod
    def getPizzaType(self):
        pass
    def __str__(self):
        "{} pizza, {} sauce, {} toppings".format(self.__class__.__type__, self.sauce, self.toppings)
class Cheese(Pizza):
    def getPizzaType(self):
        return "Cheese"
class Pepperoni(Pizza):
    def getPizzaType(self):
        return "Pepperoni"
class Cheeseburger(Pizza):
    def getPizzaType(self):
        return "Cheeseburger"
class PizzaFactory(object):
    @staticmethod
    def bake(pizzaType):
        if pizzaType == "Cheese":
            return Cheese()
        elif pizzaType == "Pepperoni":
            return Pepperoni()
        elif pizzaType == "Cheeseburger":
            return Cheeseburger()
        
for pizzaType in ("Cheese", "Pepperoni", "Cheeseburger"):
    print("{0} pizza is baking. Thank you.".format(PizzaFactory.bake(pizzaType).getPizzaType()))
