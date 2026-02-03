''' panda series is a sinfle dimensional indexed array
which can store any set of values. If index not specified
it will be defaulted to 0,1...N value.  the data can be loaded
from a database , a list , dictionary, a data frame or a CSV file.'''
import pandas as pd
# creating a panda series from a list
list=['Red','Orange','BLue']
series = pd.Series(list)
print("Series from a List:\n",series)

# Creating the series by overriding the default index
series = pd.Series(list,index=[100,101,102])
print("Series from a List:\n",series)

# Creating the series from a Dictionary
# here the key will become the index
country={'India':'Delhi','US':'Washigton','Russia':'Moscow'}
series = pd.Series(country)
print("Series from a Dictionary:\n",series)

#creating a series from a scalar value
series = pd.Series(987,index=[1,2,3])
print("Series from a Scalar:\n",series)

# Similarly series can be generated from Numpy module.
# Accessing series using index
data = pd.read_csv("Data.csv")
series = pd.Series(data["Name"])
#print("Name From CSV: \n",series)
# Selecting subsets of data prints the first 5 records
# 0~4
subsetSeries= series.head(5)
print("Subset series Name From CSV: \n",subsetSeries)
# similarly we have tail method for retrieving last X records

# Prints the series between  5 to 11
# 5~10 , 11 not included
subsetSeries= series[5:11]
print("Subset series Name From CSV: \n",subsetSeries)

#accessing the values using Iloc
subsetSeries= series.iloc[5:11]
print("Subset series using Iloc From CSV: \n",subsetSeries)

# Binary operations Add and subtract can be done on two fields
data1=pd.Series(data['Marks'])
data2=pd.Series(data['Age'])
# adds two series, fill_value used for replacing the NAN values
# before performing the desired operation
resultSeries = data1.add(data2,fill_value=0)
print("Add Result:\n",resultSeries)

resultSeries = data1.sub(data2)
print("Subtraction Result:\n",resultSeries)
# similarly we have lots of methods multiply, mean,max min etc..

resultSeries = data1.sort_values()
print("Sort Result:\n",resultSeries)

# returns the id of the max value which is 8
maxId = data1.idxmax()
print("Max Id:\n",maxId)

# returns the  max value which is 99
maxValue = data1.max()
print("Max Value:\n",maxValue)
# Similarly for string there is a method contains to check 
# for substrings

# Conversion methods helps us to convert from 
# one data type to another data type
# The below code prints the data types of the columns in CSC
before = data.dtypes
print("Data Type Before conversion:\n",before)
# The below code will work since addition of integers work
ageSeries = pd.Series(data["Age"])
age=ageSeries[1]+900
print("Age value before data conversion:\n",age)

data["Age"]= data["Age"].astype("str")


# If you notice the age column is changed from int64 to Object
# Now if you perform the addition with a int value it will throw
# an error cause a int cannot be added to a string
after = data.dtypes
print("Data Type after conversion:\n",after)

ageSeries = pd.Series(data["Age"])
print("Age Sorted after data conversion:\n",ageSeries.sort_values())

# The below code will replace the null values with the text
# "No name", also the attribute inplace=true for DF to be updated

nameSeries = pd.Series(data["Name"])
nameSeries.fillna("No Name", inplace=True)
print(nameSeries)



