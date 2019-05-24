# *args used to pass non-keyworded variable-length arguments to a function
def my_nums(*args):
    for n in args:
        print(n, end=" ")
    print(type(args))

# prints
my_nums(1,2,4,5,6)
# prints 
# '1 2 4 5 6'
# <class 'tuple'>

# **kwargs used to pass keyworded variable-length arguments to a function
def my_fullname(**kwargs):
    for key, value in kwargs.items():
        print(key + " - " + value)
    print(type(kwargs))

# prints
my_fullname(firstname="vaishu", lastname="yoshini") 
# prints 
# lastname - yoshini
# firstname - vaishu
# <class 'dict'>
