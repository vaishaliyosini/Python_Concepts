# sys module is used to parse input arguments given to a python file.
# this is used if you call a python script with arguments in command line.
import sys

firstarg  = ""
secondarg = ""
try:
    firstarg  = sys.argv[1]
    secondarg = sys.argv[2]
except:
    if (firstarg == ""):
        print("No first argument!")
    if (secondarg == ""):
        print("No second argument!")

# error text
sys.stderr.write("This is stderr text\n")
sys.stderr.flush()
sys.stdout.write("This is stdout text\n")
