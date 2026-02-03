''' This is a two dimensioanl data Tabulated with the N columns
and M rows. The rows and columns can be labelled. The columns
can have different data types, this is more like a MySQL table 
or an excel sheet. The size is mutable. 
Statistical functions, group by, aggregation can be done on 
the data using functions
'''
import pandas as pd
import matplotlib.pyplot as plt
# Empty Data Frame
df=pd.DataFrame()
print("Empty DataFrame: ", df)

# Data Frame Loaded froma list similarly it can be loaded 
# from a dictionary, ndarray, any other sequence
# rows and columns are indexed as 0..n
list=['Red','Blue','Green','Yellow']
df=pd.DataFrame(list)
print("Data frame created from a list: ",df)

# if data frame created from dictionary value should be a
# a list or array or a sequence

# The below code creates a data frame from a dictionary
# by converting it to a list
country={'India':'Delhi','US':'Washigton','Russia':'Moscow'}
df=pd.DataFrame([(k, v) for k, v in country.items()],columns=["Country","Capital"])
print("Data Frame created froma Dictionary: \n",df)

# data frame created from a list of list, each list items 
# represents a value.
students=[['Ajit','Ram',21,120],['Manoj','Kumar',20,121],['Jai','Krish',20,122]]
df = pd.DataFrame(students,columns=["First Name","Last Name", "Age", "Id"])
print("Data frame created from a list of  list: \n",df)

# Setting the row index with the id value manually using index 
# attribute
df = pd.DataFrame(students,columns=["First Name","Last Name", "Age", "Id"],index=[120,121,122])
print("Data frame created from a list of  list with index: \n",df)


df = pd.DataFrame(students,columns=["First Name","Last Name", "Age", "Id"],index=[120,121,122],dtype=float)
print("Data frame created from a list of  list with data type: \n",df)


#Creating data frame from dictionaries which has a key and list
# as a value , here each key will represent a column name and 
# the list values represent the column values.

students={'Name':['Ram','John','Mike'],'Age':[21,20,21],'id':[101,102,103]}
df = pd.DataFrame(students)
print("Data Frame created from a Dictionary:\n",df)

# with custom row index
df = pd.DataFrame(students,index=[101,102,103])
print("Data Frame created from a Dictionary with Custom index:\n",df)

# With custome columns by removing unnecessary data
df = pd.DataFrame(students,columns=["Name","id"])
print("Data Frame created from a Dictionary with few columns removed:\n",df)

# creating a data frame using the nested dictionaries
students={'CSC':{'Name':'Ram','Age':21,'id':101},
'Mech':{'Name':'Jai','Age':20,'id':102}}
df = pd.DataFrame(students)
print("Data Frame created from nested Dictionary  :\n",df)

#Creating a data frame from a dictionary which has dictionary with value as list
students={'EEE':{'Name':['Ram','John','Mike'],'Age':[21,20,21],'id':[101,102,103]},
'ECE':{'Name':['Rama','Johnny','Mikey'],'Age':[21,20,21],'id':[101,102,103]}}
df = pd.DataFrame(students)
print("Data Frame created from nested Dictionary with the values being list :\n",df)

# list of dictionaries
students=[{'Name':'Ram','Age':21,'id':101},{'Name':'Ramesh','Age':20,'id':102}]
df = pd.DataFrame(students,columns=['Name','Age','id'],index=[101,102])
print("Data Frame created from a Dictionary:\n",df)

''' IMPORTANT: dictionary keys will always be the column names.
So in the above example the keys of the dictionary is marked 
as 3 column labels. If the index name is not specified the 
the dictionary keys will be taken as column labels. If index
specified it should match with the dictionaires keys. If it 
does not match the values will be displayed as NAN.'''
print("\n")
# lets print a specific column value
print (df['Name'])

# lets print a specific row value using the row index value
print ("Values by loc \n",df.loc[101])
# the value in the loc can be a scalar,list of labels
# a slice, the below will fetch 101 and 102
print ("Values by loc slice \n",df.loc[101:103])
# a list of row labels, 101,102,103
print ("Values by loc list \n",df.loc[[102,101],])

# a list of column labels, NAme,Age
print ("Values by loc column labels\n",df.loc[:,['Name','Age']])

# a list of column labels- NAme,Age and row labels
print ("Values by loc column and Row labels\n",df.loc[[102],['Name','Age']])

# lets print a specific row value using the row index 
# this can accept static value, a list of values
# and a range of values, below is static example

print ("Values by iloc\n",df.iloc[1])

#list
print ("Values by iloc list\n",df.iloc[[0,1]])
# slice 
print ("Values by iloc slice\n",df.iloc[0:2])
# both teh columns and rows
print ("Values by iloc slice both columns and rows\n",df.iloc[0:2,1:3])


del df['Age']
print ("Age column deleted \n",df)
# similarly it can be deleted using pop function as below,
# df.pop('Age')

# Appending two data frames
students=[{'Name':'Ram','Age':21,'Id':101},{'Name':'Ramesh','Age':20,'Id':102}]
df1 = pd.DataFrame(students,columns=['Name','Age','Id'],index=[101,102])
students=[{'Name':'Priya','Age':21,'Id':103},{'Name':'Jai','Age':20,'Id':104}]
df2 = pd.DataFrame(students,columns=['Name','Age','Id'],index=[103,104])
# if no index is specified it will be 0,1,2,0,1,2..to avoid the 
# index being repeated try this  ignore_index = True
df = df1.append(df2)
print("Appended data frame: \n",df)

# Slicing data frames
print("Sliced Data: \n",df[0:3])

# Adding one extra column
# Learn more about panda series in PandaSeries.py
df['marks']= pd.Series([85,60,72,95],index=[101,102,103,104])
print("Appended Extra columns marks: \n",df)

# Iterating through the data frames will give column names
# to iterate through the row three functions are used,
# iteritems() - Displays the values of each columns and index as key/value
# iterrows() - Returns the index and the row values as a series
# itertuples() - Retrieves each row of the DF as a tuple

for row in df.itertuples():
    rowTuple=row
    print(rowTuple[0:2])# prints the 0 and 1 values of the tuple

# prints the rows in the data frame 
# , the rows are returned as series
for row_index,row in df.iterrows():
    print(row[0:2])
    print("Index: ",row_index)

for key,value in df.iteritems():
    print("Key:",key) # prints the key which is the column name
    print("Value:",value) # prints the index and the values

# Sorting data frames  by label alias row index
#  and actual value default ascending
sortedDfAscending= df.sort_index()
print("Sort By index Ascending: \n",sortedDfAscending)
#Descending sort
sortedDf= df.sort_index(ascending=False)
print("Sort By index Descending: \n",sortedDf)

''' in a data frame there are two axis , by default it sorts by
axis 0 which is the vertical axis and the row labels. In case
of axis 1 it is the column labels which is Name,Age etc...
So in the below example based on the label names the columns
are sorted'''
sortedDfAscending= df.sort_index(axis=1)
print("Sort By index Axis=1: \n",sortedDfAscending)

# Now sorting by value of a column label
sortedDfValues= df.sort_values('Name')
print("Sort By Values: \n",sortedDfValues)

# Now sorting by value of multiple columns
sortedDfValues= df.sort_values(by=['Age','Name'])
print("Sort By Values: \n",sortedDfValues)

# sorting we can specify algorithms heapsort,mergesort,quicksort
sortedDfValues= df.sort_values('Name',kind="heapsort")
print("Sort By passing algorithm: \n",sortedDfValues)

# A simple scatter plot 
#df.plot.scatter(x="Id",y="marks")
#Pie Chart
#df.plot.pie(y='marks')
# Area Chart
#df.plot.area()
# bar  chart
#df.plot.bar()
#plt.show()

#Reading CSV and converting to data frame
# the first row will be taken as header
df=pd.read_csv("Data.csv",index_col="Id")
print("\n",df)

# If the header is in a different row specify the header attribute
# header=15 

#skip rows will skip as many rows including the header
df=pd.read_csv("Data.csv",skiprows=2)
print("\n",df)





