# os module is a powerful module in python
import os

# get current working directory
print(os.getcwd()) # prints 'G:\\workspace\\Python'

# change current working directory
os.chdir("G:\\workspace\\python\\learning")
print(os.getcwd()) # prints 'G:\\workspace\\python\\learning'

# list directories in the current working directory
print(os.listdir()) # prints ['built-ins', 'Lists', 'numpy', 'strings']

# create a directory in the current working directory
os.mkdir("dicts")
os.makedirs("dicts/nested-dicts")

# remove a directory in the current working directory
os.rmdir("dicts")
os.removedirs("dicts/nested-dicts")

# rename a file or directory
os.rename("Lists", "lists")

# stats of a file or directory
os.stat("lists")
# prints 'os.stat_result(st_mode=16895, st_ino=281474977861215, st_dev=4143122855, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1480252546, st_mtime=1480252546, st_ctime=1480252090)'

# traverse a directory tree
for dirpath, dirnames, filenames in os.walk("G:\\workspace\\python\\learning"):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()

'''
prints 
Current Path:  G:\workspace\python\learning
Directories:  ['Built-ins', 'lists', 'NumPy', 'Strings']
Files:  []

Current Path:  G:\workspace\python\learning\Built-ins
Directories:  []
Files:  ['evalu.py', 'input.py', 'zipped.py']

Current Path:  G:\workspace\python\learning\lists
Directories:  []
Files:  ['list_01.py', 'tuple_01.py']

Current Path:  G:\workspace\python\learning\NumPy
Directories:  []
Files:  ['ceilr.py', 'concatenate.py', 'eye_identity.py', 'flatten.py', 'math.py', 'mean_var_std.py', 'min_max.py', 'rev_array.py', 'sum_prod.py', 'zeros_ones.py']

Current Path:  G:\workspace\python\learning\Strings
Directories:  []
Files:  ['formatting.py']
'''

# check if a file exist
print(os.path.isfile("G:\\workspace\\python\\learning\\Strings\\formatting.py"))
# prints 'True'

# check if a directory exist
print(os.path.exists("G:\\workspace\\python\\learning\\Strings"))
print(os.path.isdir("G:\\workspace\\python\\learning\\Strings"))
# both prints 'True'

# accessing environment variable
print(os.environ.get("HOME"))
# prints 'C:\\Users\\Gogul Ilango'
