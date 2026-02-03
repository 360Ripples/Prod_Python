counter =10
i=0
while i<counter:
    i+=1 # i=1
    #prints the values in the same line
    print(i, end =" ")
print()
#Important python does not support do while
#nested while loop - multiplication tabel display for 10 numbers
i=j=0
tableSwitchOn = True
# while can accept any number of conditions
while i<counter and tableSwitchOn:
    i+=1
    j=1
    print("Multiplication Table NEW:::",i)
    while j<=10:
        print(j*i,end=" ")
        j+=1
    if(i==5):
        tableSwitchOn=False
    print("Multiplication completed")
    #prints the values in the same line
    print("")
    

# printing numbers between 0 and 10 increment by 2
for i in range(0,10,2):
    print("I Value increment by 2=",i,end=" ")
print("")

# printing numbers between 0 and 10 increment by 1
for k in range(10):
    print("K Value increment by 2=:",k,end=" ")
print("")

# printing numbers between 10 and 0 decrement by 2
for i in range(10,0,2):
    print(i,end=" ")
print("")
#nested for loop multiplication
for i in range(1,11,1):
     print("Multiplication Table:::",i)
     for j in range(1,11,1):
        print(j*i,end=" ")
     print(" ")

#continue and break demo
counter =10
i=0
while i<counter:
    i+=1
    if(i%2!=0):
     continue
    #prints the values in the same line
    print(i, end =" ") 
print(" ")
counter =10
i=0
while i<counter:
    i+=1
    if(i==5):
     break
print(i, end =" ") 
