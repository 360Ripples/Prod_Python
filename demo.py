import collections

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
print(message*2)
print(message+"test")
print(message[2:])
print(message[2:5])
print(message[:7])
print(message[9])

print (message.find("cat",12))
list=["Apple","Orange",1234,4556]
print(list[0:3])
list[2]="Pineapple"
print(list[0:3])
del list[2]
print(list[0:3])
list1=[1,2,3,4,5]
for x in list1: 
    x=x*2
    print (x)
#print (cmp(list1,list))