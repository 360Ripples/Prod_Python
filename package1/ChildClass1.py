from package1.ParentClass import Employee 
class Manager (Employee):    
    #methods overrriden
    def calculateSalary(self,taxAmount):
        print("Manager calc salary invoked**")
        self.salary= self.salary*((taxAmount+10)/100)+self.salary
    
