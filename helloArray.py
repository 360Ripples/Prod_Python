import array as arr
int a = new int[2][2]


def saveNumbers():
    for i in a:
        print (" %d "%(i),end="")
    print()

def printOddNumbers():
    for i in a:
        if i%2!=0:
            print (" %d "%(i),end="")
#saveNumbers()
print ("*********Odd Numbers********")
#printOddNumbers()