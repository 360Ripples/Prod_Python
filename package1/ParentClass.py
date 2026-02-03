class Employee:
    # static class level variable
    companyName=""
    #constructor , the method arguments is the member variables
    #self should be the first argument
    #self is the class instantiated object itself.
    def __init__(self,name,empId,salary):
        self.name=name
        self.empId=empId
        self.salary=salary
#overloaded constructor is not possible
    
    #methods cannot be overloaded and it is defined as functions
    def calculateSalary(self,taxAmount):
        self.salary= self.salary*(taxAmount/100)+self.salary
    
    def displayEmployeeDetails(self):
        print("Emp Id: ", self.empId," Name: ",self.name, " Salary: ", self.salary)

    def __str__(self):
        #return "[NAME: {0}, ID: {1}, SALARY: {2}]".format(self.name,self.empId,self.salary)
        return "HEllo"
# static methods are methods which are tied to the class and not the object
# static methods does not accept any methods. It cannot change the class data members
# as per documentation it cannot access the class level variable which is company name
# but there is a workaround where we can use the class name to acces it
# as mentioed below
# primarily used as utility methods
# static methods cannot accept self parameter, so the instance data cannot 
# be accessed. If one specifies self as a method param it will be 
# considered as a int param and not the instantiated object
    @staticmethod
    def returnEmployeeString():
        Employee.companyName="ABC corp"
        return "Staic method return"
#per docuementation this can access class level variable 
# but static method cannot. But with the work 
# around both can access so i dont see any difference
# cls is the class uninstantiated itself. So it cannot access
# the instance data of the object.
    @classmethod
    def returnEmployeeValues(cls):
        cls.companyName="Class Level Company "
        cls("Jack",1234,34598)#invokes the constructor of the class
        return "class method return"+cls.companyName
# for more details on the decorators staticmethod and classmethod
# refer the below link
#https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/

''' the difference is that classmethod can create instance
of the class using the methods cls parameter. But static method
can only have logics and cannot instantiate a object.'''

