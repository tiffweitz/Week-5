class Customer:
    def __init__(self, phoneNumber, address, zipCode):
        self.phoneNumber = phoneNumber
        self.address = address
        self.zipCode = zipCode
    def getDistance(self):
        return self.zipCode

class interface:
    def confirmDelivery(self):
        "Checking delivery radius"
        
class radius(interface):
    def confirmDelivery(self):
        print("You're located within our delivery radius. Order submitted, thank you")

class CustomerProxy(interface):
    def __init__(self, customer: Customer):
        self.customer = customer
        self.radius = radius()

    def confirmDelivery(self):
        zipCode = self.customer.getDistance()
        if (zipCode == 12345 or zipCode == 12346):
            self.radius.confirmDelivery()
        else:
            print("We're sorry, you're located outside of our delivery radius.")
        
customer = Customer(123123123, "123 Pebble St", 12345)
c = CustomerProxy(customer)
c.confirmDelivery()
print ("\n")
customer2 = Customer(1231451234, "111 Elm St", 12351)
c1 = CustomerProxy(customer2)
c1.confirmDelivery()