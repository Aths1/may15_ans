#!/usr/bin/env python
# coding: utf-8

# # Machine learning -FST-5
# Grading Test -15-05-2023
Name-Atharva Kishor SalaskarQ1.A Lambda Function is a Anonymous function.
   b)Anonymous functionQ2.Why would you use the pass statement ?
   d) All of the aboveQ3.What is MRO in Python?
   b)defines the order in which the base classes are searched when executing a method.Q4.What is self in Python?
   b)Represents the instance of the classQ5.What is __init__?
   b)Constructor method in pythonQ6.What does * indicate in regular expression?
   b)Zero or more occurrences
# 
# # PART B
Q7.What is break and continue in python? Explain with example
# In[118]:


#BREAK
for i in range(1,10):
    if i==7:
        break
    print(i)


# In[119]:


#CONTINUE    
for i in range(1,10):
    if i==7:
        continue
    print(i)

8.What are Dict and List comprehensions? Give atleast one example(code)
# In[7]:


#Dictonery
Dict={"Name":"Orange","Quantity":10,"price":100}
print (Dict)
#list
list=[8,464,"Cat","Apple"]
list

9.How do you create a class in Python?class ClassName:
    # Statement10.What is inheritance ?Give  one example 
# In[144]:


class Vehicle:
    def __init__(self,price,brand):
        #print("Inside constructor")
        self.price = price
        self.rand = brand
class Car(Vehicle):
    pass
g= Car(300000,"BMW")
g.price

11.What is polymorphism? Give one example
# In[145]:


class Shape:
    def area(self,r):
        return 3.14*r*r     
    def area(self,l,b):
        return l*b
    
A=Shape()
print(A.area(3))

12.Difference between multilevel and multiple inheritance?
# In[146]:


#multilevel:
class Product:
    def review(self):
        print("product review")
class Phone(Product):
    def __init__(self,price,brand):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
    def buy(self):
        print("buying a phone")
class Sphone(Phone):
    pass

#multipleinheritance :
class Phone:
    def __init__(self,price,brand):
        print("inside the constructor")
        self.__price = price
        self.brand = brand
    def buy(self):
        print("buying a phone")
class Product:
    def review(self):
          print("Customer review")
class Sphone(Product,Phone):
    pass

13.Create a 1D,2D and 3D array?
# In[147]:


import numpy as np
#1D
a1=np.array([1,2,3,4])
print(a1)
print(a1.ndim)
#2D
a2=np.array([[1,2,3,4],[5,6,7,8]])
print(a2)
print(a2.ndim)
#3D
a3 = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]]])
print(a3)
print(a3.ndim)

14.How will you reverse the numpy array using one line of code?
# In[150]:


b=np.array([1,2,3,4])
print(b)
a=b[3:0]
print(a)

15.What advantages do NumPy arrays offer over  Python lists?
# In[ ]:




16.python3 code to print the below pattern

*
**
***
# In[12]:


for i in range(3): 
    for j in range(i+1):
        print("*",end = "")   
    print()  


# # PART C (Exploratory data analysis)
# 16.Draw insights from the dataset provided using suitable visualization libraries.(6*4 = 24)
# x: length in mm
# y: width in mm
# z: depth in mm
Q1.Load the "Diamonds dataset " from seaborn library
# In[152]:


import seaborn as sns
d=sns.load_dataset('diamonds')
d

2.Which column has highest correlation with the target variable?(Graphs)

# In[153]:


corr=d.corr()
sns.heatmap(corr)

3.Find the outliers in each column?Use suitable graphs
# In[154]:


import matplotlib.pyplot as plt
sns.boxplot(x=d['carat'])
plt.show()

sns.boxplot(x=d['depth'])
plt.show()

sns.boxplot(x=d['table'])
plt.show()

sns.boxplot(x=d['price'])
plt.show()

4.what is the count of premium diamonds in the dataset?
# In[155]:


d['cut'].value_counts()
#the count of premium diamonds in the dataset is 13791

Q5.What is the average price of diamonds?
# In[156]:


m=d['price'].mean()
m

Q6.Create a new column called "size = x*y*z
# In[157]:


d['size']=d['x']*d['y']*d['z']
d


# In[ ]:




