import re 

# multi-line string example
str = '''
Rahul is 19 years old, and Ashok is 24 years old.
Murali is 65, and his grandfather, Karthik, is 77.
'''

# findall()
ages  = re.findall(r'\d{1,3}', str)
names = re.findall(r'[A-Z][a-z]*', str) 
print (ages)  # prints ['19', '24', '65', '77']
print (names) # prints ['Rahul', 'Ashok', 'Murali', 'Karthik']

# finditer()
ages = re.finditer(r'\d{1,3}', str)
for m in ages:
    print(m.group())

# prints 
# 19
# 24
# 65
# 77

# split()
str = "This is an example string"
splitted = re.split(r'\s*', str)
print (splitted) 

# match()
str = "Dogs are braver than Cats"
matches = re.match(r'[A-Z][a-z]*', str)
print (matches.group()) # prints "Dogs"

# search()
str = "For data science help, reach support@datacamp.com"
searches = re.search(r'([\w\.-]+)@([\w\.-]+)', str)
print (searches.group())  # prints support@datacamp.com
print (searches.group(1)) # prints support
print (searches.group(2)) # prints datacamp.com



'''Identifiers

\d	any number
\D	anything but a number
\s	space
\S	anything but a space
\w	any character
\W	anything but a character
.	any character, except for a newline
\b	the whitespace around words
\.	a period
Modifiers

{1,3}	expecting 1-3 digits ~ \d{1,3}
+	match 1 or more
?	match 0 or 1
*	match 0 or more
$	match the end of a string
^	match the start of a string
|	either or (\d{1-3} | \w{5-6})
[]	range or variance
{x}	expecting "x" amount (of digits)
White Space Characters

\n	new line
\s	space
\t	tab
\e	escape
\f	form feed
\r	return
'''
