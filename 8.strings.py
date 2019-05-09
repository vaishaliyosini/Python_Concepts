# declare two strings
a = "Python"
b = " is awesome!"

print (len(a))                  # Length of the string: prints "6"
print (len(b))                  # prints "12",include space and explamatory
print (a + b)                   # String concatenation: prints "Python is awesome!"
print (a, b)                    # prints "Python  is awesome!"
print ("{}{}".format(a, b))     # prints "Python is awesome!"
print ("%s%s" % (a, b))         # sprintf style formatting: prints "Python is awesome!"
print (a.upper())               # converts all characters to uppercase: prints "PYTHON"
print (a.lower())               # converts all characters to lowercase: prints "python"
print (b.strip())               # removes trailing and leading whitespaces: prints "is awesome!"
print (b.replace("awesome", "great")) # replace a substring with a new string: prints " is great!"


'''Changed in version 3.1: The positional argument specifiers can be omitted for str.format(), so '{} {}'.format(a, b) is equivalent to '{0} {1}'.format(a, b).

Changed in version 3.4: The positional argument specifiers can be omitted for Formatter.

Some simple format string examples:

"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'''
