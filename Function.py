def add(a,b):
    return a+b
result = add(10,20)
print(result)

#default value for function
def subtract(a,b=2):
    return a-b

result = subtract(10,3)
print(result)


#multiple paramters in method
# the multiple paramter can be the last parameter of the method
def multiply(a,*d):
    total=1
    for i in d:
        total*=i # total = total*i
    return total
result = multiply(10,2,3,4,5,6,7,8,9)
print(result)


country= []
i=0
def addCountry(countryName):
    country.append("Country:"+countryName.capitalize())
    
addCountry("spain")
addCountry("germany")
addCountry("russia")
print(country)

