from package1.ChildClass1 import Employee as emp

# List is a sequence of values represented in square brackets
# List can have any values number , charachter or String
# List of Strings
fruits=['Apple','Orange','Grapes','Pineapple']

# List of numbers
numbers=[100,200,300]

# List of charachters
alphabets=['a','b','c']

#List can have values of different data type too.
numberAlpha=[1,'a',3,'b']

#Accessing values in list
lessFruits= fruits[0:2]
print (lessFruits)
print(fruits[:1])
print(fruits[2:])

#updating List the below updates the existing indes with 
# a new element
fruits[3]='Banana'
print("After add: ",fruits)
print(fruits)


#Adds a new element to the list
fruits.append('Pineapple')
print("After append: ",fruits)

# deleting element from the list
del fruits[3]
print("After Delete: ",fruits)

# Similiar to String this supports len,membership operator 
# repetition *, concatenation
#concatenationg two list
numbers = numbers + [400,500,600]
print("List concatenation: ", numbers)

print("List repetition: ",numbers*2)

print("List length: ", len(numbers))

#iteration
for i in numbers:
    print("Iterated value",i)
#member ship operator
print("membership operator value:", 600 in numbers )

#complex List structure -1 , loading list of lists
complexList=[]
complexList.append(fruits)
complexList.append(numbers)
complexList.append(alphabets)
complexList.append(numberAlpha)
print("Complex List: ", complexList)

#complex List structure -2 , loading list of lists
complexListObjects=[]
emp1 =  emp("Jack",105110,10000)
emp2 =  emp("Ron",105112,12000)
complexListObjects.append(emp1)
complexListObjects.append(emp2)
# this will print some unique identifier of the objects 
# python maintains
print("Complex Object List: ", complexListObjects)

# Python list also supports many other functions
# few example
print("Minimum Value:",min(numbers))
print("Maximum Value:",max(numbers))
# the below method will reverse all the entries of the List
# permanently
fruits.reverse()
print("Reverse List:", fruits)

# Tuples are read only sequences new elements cannot 
# be added or deleted. Only new tuples can be created 
# from existing tuples. Tuples uses paranthesis ()
# the rest of the operations and fucntions are same as list
veggies = ('Beans','Onion', 'Tomato')
print("Tuple values: ",veggies)

# Dictionary stores values as key values. Key can 
# be string, tuple or number
# duplicate keys not possible
#  
country={'India':'Delhi','US':'Washigton','Russia':'Moscow'}
print("Country Dictionary",country)
# prints the value of a key
print("India capital: ", country["India"])

# adding a new entry
country['China']='Beijing'
print("Country Dictionary",country)

# removing dictionary entries and clearing all
del country['China']
print("Country Dictionary",country)

#Clears the entire dictionary entries
country.clear()
print("Country Dictionary",country)

# This is used to delete the entire dictionary 
# del country

#Dictionary has methods like hasKey, keys() -
#  returns keys as list, values() - return values as a list
# many more methods are present too..

# Dictionary where value is a user define object
employeeDict = {"1":emp1,"2":emp2}
print("Dictionary with custom objects",employeeDict)

# Dictionary where value is a list similarly tuple can be 
# added as value
listDict = {"A":["Amber","Anu","Aye"],"B":["Bhaskar", "Bhat","Bheem"]}
print("Dictionary with List",listDict)

# prints the values in the dictionary
for x in listDict.values():
    print("Dictionary Entry: ",x)

# prints the values for the keys in the dictionary
for x in listDict:
    #print("Dictionary Keys : ",x)
    print(x,":",listDict[x])
