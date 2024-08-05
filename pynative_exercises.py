# https://pynative.com/python-pandas-exercise/

# Python Pandas Exercise
# This Pandas exercise project will help Python developers to learn and practice pandas. 
# Pandas is an open-source, BSD-licensed Python library. Pandas is a handy and useful data-structure tool for analyzing large and complex data.

# Practice DataFrame, Data Selection, Group-By, Series, Sorting, Searching, statistics. 
# Practice Data analysis using Pandas.

# In this exercise, we are using Automobile Dataset for data analysis. 
# This Dataset has different characteristics of an auto such as body-style, wheel-base, engine-type, price, mileage, horsepower, etc.

################################################# Exercise 1 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df.head(5)
df.tail(5)


################################################# Exercise 2 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

pd.set_option('display.max.rows', 200)

df.replace(['n.a','?'], '', inplace= True)
df.fillna('',inplace= True)

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv', na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)

################################################# Exercise 3 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df.groupby('company').max().sort_values(by = 'price', ascending =  False).head(1)

df = df [['company','price']][df.price==df['price'].max()]

df[['company','price']][df.price==df['price'].max()]

################################################# Exercise 4 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df_toyota = df.groupby('company').get_group('toyota')

df_toyota

################################################# Exercise 5 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df.groupby('company').count().sort_values(by = 'index', ascending = False)['index']

df['company'].value_counts()


################################################# Exercise 6 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df.groupby('company')['company','price'].max()

################################################# Exercise 7 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df.groupby('company')['company','average-mileage'].mean()

################################################# Exercise 8 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

df.sort_values(by = 'price', ascending = False).head(5)


################################################# Exercise 9 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')


GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

df_1 = pd.DataFrame.from_dict(GermanCars)
df_2 = pd.DataFrame.from_dict(japaneseCars)

new_df = pd.concat([df_1,df_2], keys = ['Ger','Jap'])

################################################# Exercise 10 #########################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\automobile_data.csv')

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

df_1 = pd.DataFrame.from_dict(Car_Price)
df_2 = pd.DataFrame.from_dict(car_Horsepower)

final_df = df_1.merge(df_2 ,on = 'Company', how= 'inner')
final_df