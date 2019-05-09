# create a class
class Customer(object):

    # init method is a must
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    # a simple print method
    def print_customer(self):
        print ("Customer: {}, Age: {}".format(self.name, self.age))

# define an instance
a = Customer("v", "2*")
a.print_customer() # prints "Customer: Gogul, Age: 2*"
