# string can be created using single or double quotes 

bookName = "Around The World In 90 Days"

# Represents a string which spans across multiple lines
bookDescription = """ This is a very boring book.
Author has dragged the story and has no logic.
Please dont read this book"""
print("Book Description", bookDescription)

#Prints the first charachter
print("Book Name First Charachter",bookName[0])

# prints the charachter between two index. It ignores the 
# charchter of the "To" index. In the below example 5
# if no starting index is give like [:5] the start index 
# by default is taken as zero
print("Book Name Charachters based on index",bookName[1:5])

# String can be resassigned to another string
authorName="Charles Dickens"
authorFirstName= authorName[:7]
print("Author First Name",authorFirstName)

# escape sequences demo \t,\v,\s,\n,\a
# insert tab space
print("Apple \t Orange")
# insert new line
print("Apple \n Orange")
#this is a back space escape sequence which deletes 
# the charachter e from apple
print("Apple\b Orange")

#concatenation of string
print(bookName+"-"+authorName)

#repetition of Strings
print(bookName*2)

#member ship returns if the given charachter
# exists in the string, the below returns True
# this is case sensitive
print("A" in (bookName))

# similarly the not in works the reverse way
# the below code returns false
print("A" not in (bookName))

# raw strings- if a charachter r is preceded the string
# the charachters in the string will be considered as raw
# string. In the below example the \n ill be ignored as a
# escape sequence
str="Apple \n Pineapple"
print (str)

# String formatting
# %d the .45 will be truncated since this formats as a int
# to display the font value us %f floating point
print("The book price is %d"%(-100.45))

# other string formatters %s - string 
# %c - ASCII value in the below example if 65 is printed 
# it is displayed as A since 65 ASCII char value is A
print(" char ASCII value- %c"%(65))
# in the below example the charchter value is printed 
# as it is
print(" char value- %c"%('C'))

# other format symbols %e exponential %0 octal 
# %x (lower case) or %X (upper case) hexa , the below example displays capital F
# if %x is used lower case f will be printed
print(" Hexa char value- %X"%(15))

# all the strings in python are represented in ascii code
# format . If we need to support multi lingual support
# we need to go for unicode . example given below
tamilchar= u"அ"
print(tamilchar)

# string functions - there are lots of string 
# functions available in python few are explained below
print("Length: ",len(bookDescription))
print("UPPER CASE: ",bookDescription.upper())
print("Count of charachters: ",bookDescription.count("a"))
# here the start and end of string is mentioned within
# which the matches to be counted.
print("Count of charachters: ",bookDescription.count("a",0,30))

# the below code snippet capitalize the first 
# charachter of the string
capitalizeString="this is a table. It has four chairs"
print("Capitalized: ",capitalizeString.capitalize())
