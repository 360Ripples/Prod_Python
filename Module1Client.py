import Module1 as a
# Second option of import from same package
#from Module1 import add,subtract
#from Module1 import *
#Modules here refers to a python file. It is always searched
# in the current directory, second it searches the PYTHONPATH variable
# Third installation folder c:\python\bin
# the _py_cache folders is a path where the module is compiled and cached
# This way the compilation phase is reduced when u run. Only 
# the execution phase will happen.
#Packages are nothing but folders which has a bunch of python files
#
import package1.Module2
#option 2 with a alias
import package1.Module2 as d
#Third option importing the package alone
# doubtful where this will be used
import package1
# Other options
from package1 import Module2 as e
#similarly you can import the function directly
from package1.Module2 import divide as div
#importing the module2 module from package 1. The advnatage is
# in this import the client wil not know what module he is importing
#There is no reference to the module2 everything is referred in the 
# init_..py file of the package 1.
#from package1 import f



result = a.add(100,20)
print("Result->",result)

result = a.subtract(100,20)
print("Result->",result)

#Package demo 1 where package is imported 
## access to module and function is done as below
result = package1.Module2.multiply(100,20)
print("Result->",result)


result = d.divide(100,20)
print("Result->",result)

result = package1.Module2.divide(300,20)
print("Result->",result)

result = e.divide(400,20)
print("Result->",result)

result = div(900,20)
print("Result->",result)

#Here the init file has the import done for all the modules
# of the package
result = d.divide(750,20)
print("Result->",result)



