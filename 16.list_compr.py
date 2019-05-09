nums = [1, 2, 3, 4, 5, 6, 7]

# traditional for loop
l = []
for n in nums:
    l.append(n)
print(l) # prints '[1, 2, 3, 4, 5, 6, 7]'

# meet list comprehension
l = [n for n in nums]
print(l) # prints '[1, 2, 3, 4, 5, 6, 7]'

# get square of each number
l = [n*n for n in nums]
print(l) # prints '[1, 4, 9, 16, 25, 36, 49]'

# same thing achieved using 'map' + 'lambda'
# 'map' means running everything in the list for a certain function
# 'lambda' means an anonymous function
l = map(lambda n: n*n, nums)
for x in l:
    print(x) 

# prints 
# 1
# 4
# 9
# 16
# 25
# 36
# 49


# using 'if' in list comprehension
l = [n for n in nums if n%2 == 0]
print(l) # prints '[2, 4, 6]'

# returning tuples with two for loops in list comprehension
l = []
for letter in "ab":
    for num in range(2):
        l.append((letter, num))
print(l) # prints '[('a', 0), ('a', 1), ('b', 0), ('b', 1)]'

# same thing using list comp
l = [(letter, num) for letter in "ab" for num in range(2)]
print(l) # prints '[('a', 0), ('a', 1), ('b', 0), ('b', 1)]
