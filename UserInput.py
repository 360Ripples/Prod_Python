''' this code  illustrates how to get input from the user
and then process into your python program.
'''
flag=True

while(flag):
    name=input("Enter Your name :")
    age = input ("Enter your age :")
    c = input("Do you want to continue (Y/N)")
    if (c=="N" or c=="n"):
        flag=False
    else:
         flag=True
    print("Name:%s, Age:%d"%(name,int(age)))
