from package1.ParentClass import Employee 
from package1.ChildClass1 import Manager 
from package1.ChildClass3 import Architect 

#class to demonstrate protected method
class SubArchitect (Architect):

  def getArchitectRegId(self):
    #the below will not work since __ is a private variable
    #return self.__architectRegistrationId;
    #the below will work since _ is a protected variable
    # and can be accessed from sub class
    return self._architectRegistrationId;

  
  def getNameChild(self):
    # the below line will throw an error since get name 
    # is marked as private
    #return self.getName();
    # the below line will work since protected methods can be 
    # accessed from sub classes
    return self._getCity();

  