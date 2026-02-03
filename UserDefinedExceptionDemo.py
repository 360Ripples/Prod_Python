# We need to create a class which extends RuntimeError or
# Exception . RuntimeError is subclass of Exception so 
# we can extend any of these classes
class EmployeeNotFoundException (Exception):
# constructors cannot be overriden so the work around is 
# add as many parameters as needed and mark it with default 
# value, so if developers want can passone or more parameters.
# The below example accepts three parameters , two have 
# been assigned default values, developers should mandatorily 
# pass one value and two arguments are optional.
    def __init__(self,exception,id="",name=""):
        self.exception=exception
        self.id=id
        self.name=name



    


