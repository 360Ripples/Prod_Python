#import sys
# set the python path for the Module 3 to work in CMD shell not
# power shell ..i.e. open cmd from windows+run and typing cmd
#C:\Users\shanmu\OneDrive\laptop\Programcontent\Python\demo
from package2.Module3 import sayHello as g

def multiply(a,b):
    return a*b;



def divide(a,b):
    return a/b;



result = g()
print("Result->",result)