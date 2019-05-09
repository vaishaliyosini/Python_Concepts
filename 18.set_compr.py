nums = [1, 1, 2, 1, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]

# traditional set (list of unique elements-omits duplicated items)
s = set()
for n in nums:
    s.add(n)
print(s) # prints {1, 2, 3, 4, 5, 6, 7, 8, 9}

# meet set comprehension
s = {n for n in nums}
print(s) # prints {1, 2, 3, 4, 5, 6, 7, 8, 9}
