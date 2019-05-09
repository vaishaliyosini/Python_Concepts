# try-except-finally
# try: test a block of code for errors.
# except: allows handling of errors.
# finally: execute code, regardless of the result of try and except blocks.
x=5
try:
    print(x)
except:
    print("Something is wrong!")



# prints 'Something is wrong!' as x is not defined

try:
    x=(3/0)
    print(x)
except: 
    print("Something is wrong!")
finally:
    print("Finally always execute after try-except.")

# prints
# Something is wrong!
# Finally always execute after try-except.
