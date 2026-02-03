from package1.ParentClass import Employee 
from package1.ChildClass1 import Manager 
from package1.ChildClass2 import Developer
from package1.ChildClass3 import Architect
from package1.ChildClass4 import SubArchitect
#Creating object instances
emp1 =  Employee("Jack",105110,10000)
emp2 =  Employee("Ron",105112,12000)



#invoking methods
emp1.displayEmployeeDetails()
emp2.displayEmployeeDetails()


#invoking salary and then displaying the employee
# details to check if the tax amount calculated is stored
# in the class level variables
emp1.calculateSalary(30)
emp1.displayEmployeeDetails()

#accessing attributes of a class
print("Employee Id= ",emp1.empId)

#invoking the Employee static method 
print("Static method invocation Return", Employee.returnEmployeeString())


#invoking the Employee class method . 
# However the method can also be invoked using the object emp1
print( Employee.returnEmployeeValues())


#setting attribute dynamically
setattr(emp1,'age',21)
print("Employee Age= ",emp1.age)

#deleting attribute dynamically
delattr(emp1,'age')

# class scoped variable is shared by all the instances of the class
# same as static but it shoudl be set using the class name
Employee.companyName="360 Ripples Solutions"

# the below prints the emp1 company 
print("Employee Company name= ",emp1.companyName)

manager =  Manager("Manager 1",105119,100000)
manager.calculateSalary(10)
manager.displayEmployeeDetails()


# creating developer using the overriden 
# constructor in child class
developer =  Developer("Developer 1",10000)
# invoking the overriden  method in child class
developer.calculateSalary(20)
# invoking the parent class method
developer.displayEmployeeDetails()


#below code is to demonstrate multiple inheritance
#in the below code always developer cosntructor is invoked
# i think it is cause of the reason it has lesser parameters
# if 3 parameters provided this throws an error
architect = Architect("Architect 1",100000)
# here the managers calcSalary is invoked because Manager
# is present in the first hiearchial chain . When the order 
# was changed and tried it was noted the developers method
# was invoked
architect.calculateSalary(10)
architect.displayEmployeeDetails()


#To demonstrate to string method. 
# This should override the __Str__ method in teh Architect class
print(str(architect))

#To demonstrate the data hiding or encapsulation
# The below code will throw a compialtion error cause 
# the architect regitration id is hidden using the prefix __
#print(architect.__architectRegistrationId)
#However it can be accessed using a method in the same class

print("Architect id:" , architect.architectID)
print("Architect Registration id:",architect._getArchitectRegIdParent())

subArchitect = SubArchitect("Aub architect", 10000)
# accessing protected variable
subArchitect.getArchitectRegId()

#accessing private method from architect
subArchitect.getNameChild()

#this accesses the protected method 
# using the instance so it will work the coding convention
# of using _ the programmer should refrain from calling the method
architect._getCity()

