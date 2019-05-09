class Customer(object):

    # this is a class variable
    raise_amount = 1.05
    num_of_custs = 0

    def __init__(self, name, age, pay):
        self.name = name
        self.age  = age
        self.pay  = pay

        Customer.num_of_custs += 1

    def apply_raise(self):
        print ("Customer {} new pay is {}".format(self.name, float(self.pay) * self.raise_amount))

if __name__ == '__main__':
    # class variable not updated
    a = Customer("G", "24", "5000")
    a.apply_raise() # prints Customer G new pay is 5250.0

    # class variable updated
    b = Customer("M", "25", "6000")
    b.raise_amount = 2.05
    b.apply_raise() # Customer M new pay is 12299.999999999998

    # print dict of an instance
    print (a.__dict__) # prints {'name': 'Gogul', 'age': '24', 'pay': '5000'}

    # There are 2 customers
    print ("There are {} customers".format(Customer.num_of_custs))
