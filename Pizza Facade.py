class OrderPizza:
    def order(self):
        pizzaType = input("What type of pizza would you like? ")
        print("Order received for {0} pizza.".format(pizzaType))
class Payment:
    def collectPayment(self):
        print("Payment has been collected, thank you.")
class MakePizza:
    def make(self):
        print("Pizza is in the oven.")
class Deliver:
    def delivery(self):
        print("Pizza has been delivered.")
class PizzaFacade:
    def __init__(self):
        self.orderPizza = OrderPizza()
        self.collectPayment = Payment()
        self.makePizza = MakePizza()
        self.deliver = Deliver()
    def pizzaOrder(self):
        self.orderPizza.order()
        self.collectPayment.collectPayment()
        self.makePizza.make()
        self.deliver.delivery()
        print("Order has been completed. Please leave a review at your convenience, thank you!")
        review = input("Were you satisfied with your order? (Y/N) ")
        if review == "Y":
            print("We are happy you enjoyed. Thank you.")
        elif review == "N":
            print("We are sorry you are unhappy. Please accept this coupon of 50% off next time.")
       
op = PizzaFacade()
op.pizzaOrder()
