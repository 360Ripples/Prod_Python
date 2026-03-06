import collections # Imports the collections module

msg="hello world"
#print(msg)

print("are u serious")

age=1020
name="shanmu"
salary=200.345
print(age)
print("name",name)
print("age",age)
print("salary",salary)

a=b=c=100
d,e,f=2,3,4
print(a,b,c,d,e,f)

message="The cat is sitting on the wall"
print(message*2) #prints the message two times
print(message+"test") # concatenation
print(message[2:])# prints from index 2 to end
print(message[2:5])#   prints from index 2 to 4
print(message[:7])# prints from start to index 6
print(message[9])# prints character at index 
print(len(message))# prints length of the string
print(message.upper())# converts to upper case
print (message.find("cat",12))# finds the index of substring cat starting from index 12

# list can have multiple data types
list=["Apple","Orange",1234,4556]

print(list[0:3])
list[2]="Pineapple"# modify the value at index 2
print(list[0:3])#   prints from index 0 to 2

del list[2]# delete the value at index 2
print(list[0:3])

list1=[1,2,3,4,5]
for x in list1: 
    x=x*2
    print (x)
print (list1==list)# compares two lists
list2=[1,2,3,4,5]
print (list1==list2)