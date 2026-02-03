# A module is nothing but a simple python file which 
# encompasses one or more functions or classes 
#  and logically group the code. The modules needs to be 
# imported in other files to be used.
# The file needs to be imported should have its path
#  specifed in the PYTHONPATH environemental variable (or)
# the file should be available in the current directory 
# where the file is imported (or) should be in the python 
# installation path example c:\python\
# PythonPath is the ideal way of doing this.

# A package is the directory structure where the python 
# file or module is placed. A package can have any sub packages.
# to access a module which is under a package the pyhtonpath 
# variable should be defined till the root package.
# Example if mod1 is in package d:\test\com, 
# pythonPath should be defined as d:\test 
# so import as "from com import mod1 as mod1Alias"
def add(a,b):
    return a+b

#default value for function
def subtract(a,b=2):
    return a-b

