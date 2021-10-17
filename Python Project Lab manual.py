#!/usr/bin/env python
# coding: utf-8

# **Create a pandas series from a dictionary of values and ndarray**

# In[3]:


import pandas as pd
import numpy as np
myArr = np.array([23,1,9,80,48,67])
s = pd.Series(myArr)
print(s)
#create dictionary
dictionary = {'A':10, 'B':20,'C':30}

#create a series from dictionary
series = pd.Series(dictionary)

print(series)


# #2 **Given a Series, print all the element that are above the 75th percentile

# In[4]:


#import pandas and numpy
import pandas as pd
import numpy as np
s = pd.Series(np.array([1,3,4,5,6,8,8]))
print(s)

res = s.quantile(q=0.75)
#the element that are above the 75th precentile

print("The element that are above the 75 percentile:-")
print(s[s>res])


# **Create a Data Frame quaterly sales where each row contains the  item category. item name, and expenditure. Group the rows by the category

# In[23]:


import pandas as pd
dic= { "itemcat":["car","Mobile Phone" "Washing Machine", "TV"],
        "itemname" : ["ford", "Hitachi", "Symphony", "LG"],
       "expenditure":[700000, 50000, 20000, 50000]}
quartSales = pd.DataFrame.from_dict(dic,orient='index')
print(quartSales)
qs=quartSales.groupby("itemcat")
       
print("Result after Filterings Dataframe")
print(qs["itemcat", "expenditure"].sum())


# Create a dataframe based on ecommerce data and generate descriptive statistics(mean, meridian, mode, quartile and variance).

# In[ ]:


import pandas as pd
sales = { "invoice":[1001,1002,1003,1004,1005,1006,1007],
          "ProductName" : ["Led", "AC", "deodrant", "jeans", "Books", "Shoes","Jacket" ],
         "Quantity": [2,1,3,5,8,5,4],
         "Price": [65000, 55000, 1000, 2500, 950, 4000, 2200]}
df = pd.DataFrame(sales)
print(df["Price"].describe().round(2))
    
    
    


# #5 **Create a dataframe for examination result and display row labels, column labels data types of each column and the dimensions

# In[28]:


import pandas as pd
dic = {"Class":["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"],
       "Pass-Percentage": [100,100,100,98,99,98,97,100,100,99,96.5,100]}
result = pd.DataFrame(dic)
print(result)
print(result.dtypes)
print("shape of the Dataframe:")
print(result.shape)


# #7 Find the sum of each column, or find the column with the lowest mean.

# In[40]:


import pandas as pd
profit = {"TCS": {"Qtr1":2500, "Qtr2": 2000, "Qtr3" : 3000, "Qtr4":2500},
          "WIPRO": {"Qtr1":2800, "Qtr2": 2400, "Qtr3":3600, "Qtr4":2500},
          "L&T": {"Qtr1":2100, "Qtr2": 5700, "Qtr3":3500, "Qtr4":2100} }
df = pd.DataFrame(profit)
print(df)
print()
print("Column wise sum in DataFrame is: ")
print(df.sum(axis=0)
#print mean value of each column
print()
print("Column wise mean value are: ")
print(df.mean(axis=0))
print()
print("Column with minimum mean value is ")
print(df.mean(axis=0).idxmin())
         


# #8 Locate the 3 largest values in a DataFrame

# In[42]:


import pandas as pd
dic = {"Name": ["Rohit", "Mohit", "Deepak", "Aditya", "Akshita", "Yash"],
       "MarksInIp"  : [ 85,45,92,89,88,94]}
marks = pd.DataFrame(dic)
#Find the 3 largest value for marks in IP Column
print(marks.nlargest(3,["MarksInIp"]))
      


# Subtract the mean of a row from each element of the row in a DataFrame.

# In[47]:


import pandas as pd
import pandas as pd
profit = {"TCS": {"Qtr1":2500, "Qtr2": 2000, "Qtr3" : 3000, "Qtr4":2500},
          "WIPRO": {"Qtr1":2800, "Qtr2": 2400, "Qtr3":3600, "Qtr4":2500},
          "L&T": {"Qtr1":2100, "Qtr2": 5700, "Qtr3":3500, "Qtr4":2100} }
df = pd.DataFrame(profit)
print(df)
print()
print('Mean of each row is:')
print(df.mean(axis=1))
print()
print("Dataframe after subtracting mean value of each row of that row is:")
print(df.sub(df.mean(axis=1), axis = 0))


# #10 Replace all negative value in a DataFrame with a 0

# In[49]:


import pandas as pd
dic = {"data1" : [-5,-2,5,8,9,-6],
       "data2" : [2,4,10,15,-5,-8]
      }

df = pd.DataFrame(dic)
print(df)
print()
print("DataFrame after replacing negative values with 0 :")
df[df<0]=0
print(df)


# #11 Replace all missing values in a dataframe with 999

# In[50]:


import pandas as pd
import numpy as np
empData = {"empid" : [101,102,103,104,105,106],
            "eName": ["sachin","Yash", "Prashi", np.nan, "Ansh", "Chetna"],
           "Dob" : ["12-02-2005", "15-10-2004", "11-08-2003","1-02-2005","22-05-2005","13-07-2002"]}
df = pd.DataFrame(empData)
print(df)
df = df.fillna({"eName" : 999, "Dob": 999})
print()
print(df)


# #12 importing and exporting data between pandas and CSV file

# In[51]:


import pandas as pd
df = pd.read_csv("G:\ip csv file .csv")
print(df)


# In[55]:


import pandas as pd
list = [{"FirstName" : "Sachin", "lastname" : "Bhardwaj"},
        {"FirstName" : "Vinod", "lastname" : "Verma"},
        {"FirstName" : "Shreya", "lastname" : "Pandey"}
       ]
df1 = pd.DataFrame(list)
#saving the datagframe
df1.to_csv("G:\ip csv file .csv")


# In[ ]:





# #13 importing and exporting data between pandas and Mysql database.

# In[59]:


import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='localhost')


# In[60]:


import mysql.connector


# In[61]:


-m pip install mysql-connector-python


# In[62]:


pip install mysql-connector-python


# In[65]:


import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='localhost', database="sachin")


# In[64]:


emp = pd.read_sql_query("Show tables from sachin",con)


# In[67]:


import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost', database="sachin")


# #14 Given the school resukt data, analyse the performance of the students on different parameters, e.g. subject wise or class or wise

# In[68]:


pip install matplotlib


# In[74]:


import matplotlib.pyplot as plt
Subject = ["Physics", "Chemistry", "Mathematics", "English", "Computer science"]
Percentage = [90,78,90,100,100]
plt.bar(Subject,Percentage, align = "center", color="green")
plt.xlabel("Subject Name")
plt.ylabel("Pass Percentage")
plt.title("Bar Graph for Result Analysis")
plt.show()


# #bar/plot bug in jupyter notebook : https://github.com/matplotlib/matplotlib/issues/16458

# #15 For the data frame created above, analyze and plot appropriate charts with title and legend
# 

# In[77]:


import matplotlib.pyplot as plt
import numpy as np
s = ['1st', '2nd', '3rd']
per_sc = [95,89,77]
per_com = [90,93,75]
per_hum = [97,92,89]
x = np.arange(len(s))
plt.bar(x,per_sc,label="Science", width = 0.25, color = "green")
plt.bar(x+.25, per_com, label="Commerce", width = 0.25, color="red")
plt.bar(x+.50, per_hum, label="Humanities", width =0.25, color="gold")
plt.xticks(x,s)
plt.xlabel("Position")
plt.ylabel("Percentage")
plt.title("Bar graph for result analysis")
plt.legend()
plt.show()


# In[ ]:




