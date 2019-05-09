# I need to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9]

# traditional generator function
def gen_func(nums):
    for n in nums:
        yield n*n

m = gen_func(nums)
for i in m:
    print(i)

# generator expression
m = (n*n for n in nums)
for i in m:
    print(i)

'''
both prints 
1 
4 
9 
16
25
36
49
64
81
'''
