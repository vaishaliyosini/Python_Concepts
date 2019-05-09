# declare a tuple
t = (500, 200)

print (type(t))    # prints "<type 'tuple'>"
print (t[1])       # prints 200

# tuple of tuples
tt = ((200,100), t)

print (tt)         # prints "((200, 100), (500, 200))"
print (tt[1])      # prints "(500, 200)"

# loop over tuple
for item in t:
    print (item)   # prints each item in the tuple


# built-in tuple commands
print (len(t)) # prints the length of tuple which is 2
print (max(t)) # prints the max-valued element which is 500
print (min(t)) # prints the min-valued element which is 200

# convert list to tuple
l = [400, 800, 1200]
l_to_t = tuple(l)

print (type(l_to_t))# prints <class 'tuple'>
