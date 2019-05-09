# declare a list
l = [1,2,3,4,5]

# length of list
print (len(l))      # prints "5"

# indexing
print (l[0])        # prints "1"
print (l[1])        # prints "2"
print (l[len(l)-1]) # prints "5" last element
print (l[-1])       # negative indexing: prints "5"

# insert and remove
l.append(6)        # inserts "6" at last
print (l)            # prints "[1,2,3,4,5,6]"
item = l.pop()     # removes last element and returns that element
print (item)         # prints "6"
l.append("string") # adds different data type too
print (l)           # prints "[1,2,3,4,5,'string']"
l.pop()            # removes last string element

# slicing list
print (l[1:2])       # prints "2"
print (l[1:3])       # prints "2,3"
print (l[0:])        # prints "[1,2,3,4,5]"
print (l[0:-1])      # prints "[1,2,3,4]"
print (l[:])         # prints "[1,2,3,4,5]"

# loop over the list
for item in l:
    print (item)     # prints each item in list one by one

# enumerate over the list
for i, item in enumerate(l):
    print ("{}-{}".format(i, item)) # prints each item with its index

'''A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task.
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. '''
# changing start index to 2 from 0 
print (list(enumerate(l,2)) )

# squaring elements in a list
for item in l:
    if item%2 == 0:
        print (item**2)      # square each even number in the list

# above can be achieved using a list comprehension too! (one-line)
#print ([x2 for x in l if x%2==0])

# sort the list
b = [5, 7, 2, 4, 9]

# ascending order
b.sort()
print (b)  # prints [2, 4, 5, 7, 9]

# descending order
b.sort(reverse=True)
print (b) # prints [9, 7, 5, 4, 2]

# reverse the list (notice this is not descending order sort)
a = ["dhoni", "sachin", "warner", "abd"]
a.reverse()
print (a) # prints ['abd', 'warner', 'sachin', 'dhoni']

# count of object in list
a = [66, 55, 44, 22, 11, 55, 22] 
print (a.count(22)) # prints 2
