from package1.ParentClass import Employee 
from package1.ChildClass1 import Manager 
class Developer (Employee):
#overriden constructor
  def __init__(self,name,salary):
        self.name=name
        self.empId=999
        self.salary=salary    
    #methods overrriden
  def calculateSalary(self,taxAmount):
      print("Developer calc salary invoded**")
      self.salary= self.salary*((taxAmount-10)/100)+self.salary
    

