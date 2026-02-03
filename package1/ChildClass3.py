from package1.ParentClass import Employee 
from package1.ChildClass1 import Manager 
from package1.ChildClass2 import Developer 

#class extends two classes demonstrate multiple 
# inheritance
class Architect (Manager,Developer):

  # __ underscore prefix makes a variable private
  # can be accessed by methods of the same class alone
  # but again it can be accessed using the instance variable
  # It is upto the developers to avoid accessing it

  __architectRegistrationId=100
  # single under score prefix is that it is protected
  # and can be accessed form same class or sub class
  # but again it can be accessed using the instance variable
  # It is upto the developers to avoid accessing it  
  _architectRegistrationId=1001
  architectID=99;
  

  def _getArchitectRegIdParent(self):
    return Architect.__architectRegistrationId

  def buildSoftware(self):
      print("I am building software");
  #This is as good as ToString method
  def __str__(self):
    return "Architect Object:[Emp ID: "+str(self.empId)+" Emp Name:"+self.name+"]"
#private method marked with prefix __. 
# Cannot be accessed outside even with instance variable
  def __getName(self):
    return "Private method name"
#protected method marked as _
# can be accessed by subclasses alone
# This method can be accessed by creating 
# a instance of this class , refer CLassMain class
# It is upto the developers to avoid accessing it 
# outtside the class

  def _getCity(self):
    return "Chennai";