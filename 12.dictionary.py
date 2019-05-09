# declare a dictionary
d = { "1" : "Ironman", 
      "2" : "Captain America", 
      "3" : "Thor"
    }

print (type(d))    # prints "<type 'dict'>"
print (d["1"])     # prints "Ironman"

# loop over dictionary
for key in d:
    print (key)   # prints each key in d
    print (d[key]) # prints value of each key in d (unsorted)

# change values in the dictionary
d["2"] = "Hulk"
for key, value in d.items():
    print(key + " - " + value)

'''
prints
1 - Ironman
2 - Hulk
3 - Thor
'''

# check if key exists in a dictionary
if "3" in d:
    print("Yes! 3 is " + d["3"])
# prints 'Yes! 3 is Thor'

# get length of the dictionary
print(len(d)) # prints 3

# insert a key-value pair to a dictionary
d["4"] = "Thanos"

# remove a key-value pair from the dictionary
d.pop("4")

# same thing using 'del' keyword
del d["2"]

# clear a dictionary
d.clear()

