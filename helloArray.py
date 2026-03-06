import array as arr

a = [[1, 2, 3],
     [4, 5, 6]]

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