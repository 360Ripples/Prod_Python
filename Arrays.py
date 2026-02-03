#Python does not support native arrays it is achieved using 
# the List object which is explained below
# integer array
numbers = [222,111,333,444,555];

#iterating an array in printing it

for i in numbers:
    print(i);

#print the length of the array
print("Array Length-->",len(numbers));
#print a specific element of the array
print("Element 3", numbers[2]);

#remove a element from the array, this removes the number 
# 444 from the list index starts from 0
numbers.pop(3);

#second option removes the value 333 fromt the list
#numbers.remove(333);
print(numbers);


# other methods are insert(position,value), sort(),reverse()
# count(value) - returns how many times the value is in the list

#2d array declaration it is as good as list within another list
cols=3
rows=3
matrix =[[0 for i in range(cols)] for j in range(rows) ]
print(matrix)

#adding a element in the array
matrix[0][0]=10;
matrix[1][1]=99;
print(matrix)


for i in matrix:
    print("Rows::",i);

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ");
    print("");
