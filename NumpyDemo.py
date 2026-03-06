'''numpy stands for numerical python, a third party
open source library created by Travis Oliphant .It stores data in single and
 multidimensional array on which many numerical
,linear algibra and statistical functions be applied. Useful
for people building algorithms.
In addition to this numpy supports different numeric data types 
such as int32,int,int64,uint32,float16 etc..'''
import numpy as np

# single dimensional array
evenNumber=np.array([12,14,2,4,16,6,8,10])
print("Numpy array from a list: ",evenNumber)

# 2*2 dimensional array/matrix
evenNumberMatrix = np.array([[2,4],[6,8]])
print("Numpy array 2*2 matrix/array:\n",evenNumberMatrix)

# single dimensional array declared with data type float16
evenNumber=np.array([12,14,2,4,16,6,8,10],dtype=np.float16)
print("Numpy array from a list: ",evenNumber)

#Defining a structured data type and using it
ageDT=np.dtype([('Age',np.int64)])
ageArray= np.array([23,34,21,42,18,16],dtype=ageDT)
print("Custom scalar data type: ",ageArray)

# Defining structured composite data type
studentdt=np.dtype([('Age',np.int8),('Name',object),('Marks',np.float16)])
studentArray = np.array([(21,"Jack",96.5),(19,"Tina",35.4)],dtype=studentdt)
print("Student Array: ",studentArray)

# Automatic arrays
autoArray = np.zeros((3,3))
print("ZEROES ARRAY",autoArray);
autoArray = np.ones((3,3))
print("ONES ARRAY",autoArray);

# populate a Array with a range of numbers
rangeArray = np.arange(1,10); # single dimension array
print(rangeArray);

rangeArray = np.arange(1,30,2); # load array with step of 2
print("LOAD ARRAY STEP 2",rangeArray);

#reshape
rangeArray = np.arange(1,13,1).reshape(3,4); # reshape array to 3X4
print("RESHAPED:",rangeArray);

#Indexing
autoArray=np.arange(1,11);
print(autoArray);
print(autoArray[9]);
print(rangeArray[2,1]);

#shape
print("SHAPE:",rangeArray.shape)

#Vectorization -Vectorization in NumPy means performing 
# operations on entire arrays at once instead of using loops.
a = np.array([1,2,3]);
b = np.array([4,5,6]);

print("Vectorized array",a+b) ;
#Scaler operation
print("Vectorized array Scalar",a*2) ;

# vactorization a> 4
a = np.array([1,2,3,4,5,6,7,8]);
print("Vectorized array Condition check",a[a>4]) ;

# vactorization Even numbers alone
a = np.array([1,2,3,4,5,6,7,8]);
print("Vectorized array Condition check",a[a%2==0]) ;

print("Vectorized array Condition check",a[a%2==0]+1) ;

#numpy array filtering
a = np.array([2,7,3,9,1,8]);
result = np.where(a%2==0 , 'x', a);
print("Filtered array",result);

#Fast column operation
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("Column 3 array",a[:,2]);
print("Row 3 array",a[2,:]);

# Row / Column Sum (Axis)
print("Column ro sums",np.sum(a,axis=0));
print("Row ro sums",np.sum(a,axis=1));

#Multiplication
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])
print("Multiplication:",np.dot(a,b))


#Functions
#Each row (axis = 1)= student
#Each column (axis = 0) = subject
marks = np.array([
[85,78,90],
[88,76,92],
[90,82,85]
])

print("Total marks Students: ",np.sum(marks,axis=1));
print("Average marks Students: ",np.mean(marks,axis=1));
print("Average marks subject wise: ",np.mean(marks,axis=0));
print("Max mark: ",np.max(marks));
print("Max mark of each student: ",np.max(marks,axis=1));

#statistical functions
print("Median value student wise marks: ",np.median(marks,axis=1));
print("SD value student wise marks: ",np.std(marks,axis=1));

#boolean Functions

print("Marks > 90",np.any(marks>=90,axis=1));
print("ALL MArks > 90",np.all(marks>=90,axis=1));

# unique and sorting
print("Marks sort student wise ",np.sort(marks,axis=1));
print("Marks unique student wise ",np.unique(marks));
