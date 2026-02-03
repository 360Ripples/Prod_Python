''' Python supports exception handling this code
is to give a demo on how exception is handled in programs
. In case of any exception python program exits abrubtly
if we need the program to handle this exception and elegantly
process it we need to use exception handling. Exception is the base 
class of all the exceptions, it is nothing but error when running
the program. Some sub classes of exception are
ArithmeticError when numerical error happens, ZeroDivisionError,
KeyError when key is not found in a dicitionary, SyntaxError error
when the syntax of the python is wrong,IndentationError when 
indentation is wrong, NameError when a variable is not defined
, Type Error when a data is not ble to be converted to another 
example int to string.'''

from UserDefinedExceptionDemo import EmployeeNotFoundException
#Exception handling using try and exception
def divide(a,b):
    try:
        c=a/b
        print("Result->",c)
    except ZeroDivisionError as error:
        print("Error happened when dividing:",error)

# below code will siumlate the error
divide(10,0)

# Exception handling using try , exception and else
# else block is executed in case if there is no exception
def divideElse(a,b):
    try:
        c=a/b
        print("Result->",c)
    except ZeroDivisionError as error:
        print("Error happened when dividing:",error)
    else:
        print("No Error")
divideElse(10,20)

# Exception handling using try,excpetion and finally
# finally is executed irrespective of error happens or not
# Else cannot be used along with finally
def divideFinally(a,b):
    try:
        c=a/b
        print("Result->",c)
    except ZeroDivisionError as error:
        print("Error happened when dividing:",error)
    finally:
        print("****Finally block****")

#finally block will be invoked without error
divideFinally(10,20)

#finally block will be invoked with error
divideFinally(10,0)

# multiple exception handling, here name error will
# be thrown as variable d is not defined
def multipleException(a,b):
    try:
        c=a/b
        c=c+d
        print("Result->",c)
    except ZeroDivisionError as error:
        print("Zero Division Error happened when dividing:",error)
    except NameError as error:
        print("Name Error happened when dividing:",error)
    finally:
        print("****Finally block****")
multipleException(10,20)
#instead of catching all exceptions the base exception 
# can be caught as below
def genericException(a,b):
    try:
        c=a/b
        c=c+d
        print("Result->",c)
    except Exception as error:
        print("General Exception happened when dividing:",error)
# simulating division by zero error
genericException(10,0)

# simulating division by name error
genericException(10,10)

# the below code demonstrates how exception be raised 
# using raise keyword. A  exception class/object
# can be raised as an error

def raiseError(a,b):
    if(b <= 0 ):
        raise Exception("Divisor cannot be zero is raised")
    else:
        c=a/b

#This will throw the user raised error
#raiseError(10,0)

# Refer this link for the exception hiearchy
# https://airbrake.io/blog/python-exception-handling/class-hierarchy

# Lets raise a user defined exception
def findEmployees(employeeId,name):
    if employeeId <=0 or employeeId is None:
        raise EmployeeNotFoundException("Employee not found",employeeId)
    else:
        print("User Defined Exception not thrown")
# lets simulate the user defined exception
# IMPORTANT: PLEASE COMMENT THE RAISE ERROR IN THE 
# PREVIOUS METHOD FOR THIS TO WORK. The python program will
# abrubtly stop, else in the above raise error use try block
# to handle it
try:
    findEmployees(0,"jack")
except EmployeeNotFoundException as e:
    print("Exception happened During employee search-->",e)

