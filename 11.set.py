# set is a collection of unordered and unindexed data which is written with curly brackets.
s = {"ironman", "hulk", "thor", "thanos"}

for x in s:
    print(x)

'''
prints 
ironman
thor
hulk
thanos
'''

# check if value exist in set
if "thanos" in s:
    print("endgame") # prints 'endgame'

# add a single item to a set using 'add'
s.add("rocket")

# add multiple items to a set using 'update'
s.update(["blackhood", "blackwidow"])

# get length of a set
print(len(s)) # prints 7

# 'remove' or 'discard' an item from the set
# 'remove' raise an error if item to remove does not exist
# 'discard' will not raise any error if item to remove does not exist
s.remove("thanos")
s.discard("blackwidow")

# clear the set
s.clear()

# delete the set
del s
