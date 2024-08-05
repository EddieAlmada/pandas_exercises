import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\countries of the world.csv')

df_txt = pd.read_table(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\countries of the world.txt')

df_json = pd.read_json(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\json_sample.json')

df_excel = pd.read_excel(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\world_population_excel_workbook.xlsx', sheet_name= 'Sheet1')

pd.set_option('display.max.rows', 235)

df_excel.info()

df_excel.shape

df_excel["Rank"]

######################################## Filtering ###################################
import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\world_population.csv')

df[df['Rank'] <= 10]

specific_contries = ['Bangladesh', 'Brazil']

df[df['Country'].isin(specific_contries)]

df[df['Country'].str.contains("United")]

df_2 = df.set_index('Country')

df_2.filter(items = ['Continent', 'CCA3'], axis = 1)

df_2.filter(items = ['Zimbabwe'], axis = 0)

df_2.filter(like = 'United', axis = 0)

df_2.loc['United States']

df_2.iloc[3]

df[df['Rank'] < 10].sort_values(by = ['Continent', 'Country'], ascending = [False, True])

######################################## Indexing ###################################

import pandas as pd 

df = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\world_population.csv')

ddf = pd.read_csv(url, index_col= 'Country')

df.reset_index(inplace=True)

df.set_index('Country', inplace = True)

df.loc['Albania']
df.iloc[1]

df.reset_index(inplace = True)

df.set_index(['Continent', 'Country'], inplace = True)
df.sort_index()

pd.set_option('display.max.columns', 235)

######################################## Group By ###################################

import pandas as pd

df = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\Flavors.csv')

group_by_frame = df.groupby('Base Flavor')

group_by_frame.mean()

df.groupby('Base Flavor').mean()

df.groupby('Base Flavor').count()

df.groupby('Base Flavor').median()

df.groupby('Base Flavor').min()

df.groupby('Base Flavor').max()

df.groupby('Base Flavor').sum()

df.groupby('Base Flavor').agg({'Flavor Rating': ['mean','max','sum','count'], 'Texture Rating': ['mean','sum','count']})


df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating': ['mean','max','sum','count']})

df.groupby('Base Flavor').describe()

######################################## Merging DF ###################################

import pandas as pd

df_1 = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\LOTR.csv')
df_2 = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\LOTR 2.csv')

df_1
df_2

df_1.merge(df_2, how = 'inner')
df_1.merge(df_2, how = 'inner', on = ['FellowshipID', 'FirstName'])

df_1.merge(df_2, how = 'outer', on = ['FellowshipID', 'FirstName'])

df_1.merge(df_2, how = 'left', on = ['FellowshipID', 'FirstName'])
df_1.merge(df_2, how = 'right', on = ['FellowshipID', 'FirstName'])


df_1.merge(df_2, how = 'cross')


df_1.join(df_2, on = 'FellowshipID', how = 'outer', lsuffix = '_left', rsuffix = '_right')


df_4 = df_1.set_index('FellowshipID').join(df_2.set_index('FellowshipID'),  lsuffix = '_left', rsuffix = '_right', how = 'outer')
df_4

pd.concat([df_1,df_2], join = 'outer', axis = 1)

df_1.append(df_2)


######################################## Visualization ###################################

import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\Ice Cream Ratings.csv')

df = df.set_index('Date')
df

df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Value')

df['Flavor Rating'].plot(kind = 'bar', stacked = True )

df.plot.barh(stacked = True )

df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 100, c = 'Green')

df.plot.hist(bin = 20)

df.boxplot()
df.plot.area(figsize = (10,5))
df.plot.pie(y = 'Flavor Rating', figsize = (10,6))

######################################## Data Cleaning ###################################

import pandas as pd

df = pd.read_excel(r'C:\Users\almad\Documents\repos\edx-ibm-python-scripts\pandas_youtube_series\Customer Call List.xlsx')

pd.set_option('display.max.rows', 20)
pd.set_option('display.max.columns', 10)

df.drop_duplicates(inplace = True)
df.drop(columns = 'Not_Useful_Column', inplace =  True)
df
# df['Last_Name'] = df['Last_Name'].str.lstrip('...')
# df['Last_Name'] = df['Last_Name'].str.lstrip('/')
# df['Last_Name'] = df['Last_Name'].str.rstrip('_')

df['Last_Name']
df['Last_Name'] = df['Last_Name'].str.strip('123._/')
df['Last_Name']

df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')

df

df[['Street_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',', 2, expand = True)

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')


df.replace('N/a', '', inplace = True)
df.fillna('', inplace = True)

for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace = True)
else:
    pass

for x in df.index:
    if df.loc[x, 'Phone_Number'] == '':
        df.drop(x, inplace = True)
else:
    pass

df.dropna(subset = 'Phone_Number', inplace = True)

df.drop(columns = 'Address', inplace = True)

df.reset_index(drop = True, inplace =  True)

df

######################################## Exploratory Data Analysis ###################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\almad\Documents\repos\pandas_exercises\world_population.csv')

df

pd.set_option('display.float_format', lambda x: '%.2f' % x)

df.info()
df.describe()

df.isnull().sum()

df.nunique()

df.sort_values(by = '2022 Population', ascending = False).head(10)

df.corr()
sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (15,7)
plt.show()

df2 = df.groupby('Continent')['1970 Population', '1980 Population',
       '1990 Population', '2000 Population', '2010 Population',
       '2015 Population', '2020 Population', '2022 Population'].mean().sort_values(by = '2022 Population', ascending = False)

df[df['Continent'].str.contains("Oceania")]

df2.plot()
plt.show()

df.columns

df3 = df2.transpose()
df3.plot()



df.boxplot()

plt.show()

df.dtypes
df.select_dtypes(include = 'number')