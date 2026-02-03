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
studentdt=np.dtype([('Age',np.int8),('Name',np.object),('Marks',np.float16)])
studentArray = np.array([(21,"Jack",96.5),(19,"Tina",35.4)],dtype=studentdt)
print("Student Array: ",studentArray)

#for more on arithmetic , algebric, statistial function
# browse the python numpi API.
