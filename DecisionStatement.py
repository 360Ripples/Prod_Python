a,b,c=10,20,30;

if (a>b):
 print("A is greater")
else:
 print("B is greater")

 # if with else if and logical operator
 if(a>b and a>c):
     print("A is greater")
 elif (b>a and b>c):
     print("b is greater")
 else:
     print("C is greater")

#if using or operator

 # if with else if and OR  logical operator
 if(a>b or a>c):
     print("A is greater")
 elif (b>a or b>c):
     print("b is greater")
 else:
     print("C is greater")

#equivalent to ternary operator
print ("A is greater ternary") if (a>b) else print("B is greater ternary")


#NOT operator
if (not(a>b)):
 print("NOT: B is greater")
else:
 print("NOT: A is greater")

#NESTED IF elsif

if(a>b):
    if(a>c):
        print("Nested: A is greater")
    else:
        print("Nested: C is greater")
elif (b>a):
    if(b>c):
        print("Nested: B is greater")
    else:
        print("Nested: C is greater")
 