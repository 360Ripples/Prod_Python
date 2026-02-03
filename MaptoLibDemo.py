import matplotlib.pyplot as pt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Code to plot a line graph
np1= np.array([2014,2015,2016,2017,2018])
np2= np.array([9.0,8.5,7.5,8.5,4.5])
pt.title("My First Plot")
pt.xlabel="Year"
pt.ylabel="GDP Growth"
# if we remove go - green dots ro- red dots etc,
#  it will be a line graph
#pt.plot(np1,np2,"ro")

#Creating sub plots
np3= np.array([10,20,30,40])
np4= np.array([2,5,3,7])

#pt.subplot(1,2,1)
#pt.plot(np1,np2,"bo")
#pt.subplot(1,2,2)
#pt.plot(np3,np4,"go")

# bar graph
#pt.bar(np1,np2,color="red")
#barh for horizonatl bar
#pt.barh(np1,np2,color="red")

#print two bar plaot in the same figure
divisions= np.array([2014,2015,2016,2017,2018])
np5= np.array([9.0,8.5,7.5,8.5,4.5])
np6= np.array([4.0,5.5,7.5,4.5,8.5])
index=np.arange(5)# gives evenly spaced 5 values
width=0.3

#pt.bar(index,np5,width,color="green",label="US Economy")
#pt.bar(index+width,np6,width,color="orange",label="Indian Economy")

#vertically stacked graph
#pt.bar(index,np5,width,color="green",label="US Economy")
#pt.bar(index,np6,width,color="orange",label="Indian Economy",bottom=np5)
#pt.legend(loc="best")

# pie chart
#pt.pie(np5,explode=None, labels=np1,shadow=True,startangle=45,radius=0.75)
#pt.legend(title="Year",loc="upper left")

#scatter plot

np7=np.array([10,20,15,30,5])
np8=np.array([2,4,6,8,10])
#pt.scatter(np7,np8)

#3d scatter
ax=pt.axes(projection='3d',label="Demo")
ax.scatter3D(np7,np8)
ax.set_xlabel("age")
ax.set_ylabel("BMI")

pt.show()

