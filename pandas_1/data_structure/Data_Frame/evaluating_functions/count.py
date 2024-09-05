# count of a particular element in a column

# new_df = old_df.groupby('column_name) ['column_name'].count()

import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/sample4.txt', sep=',', header=None)
df.columns = ['Id','fname','lname','age','phno','location']

df1 = df.groupby('location') ['location'].count() # count of each location
print(df1)

df2 = df.groupby('age') ['age'].count() # count of each age
print(df2)

df3 = df.groupby('location') ['location'].count().sort_values() # ascending sort count
print(df3)

df4 = df.groupby('location') ['location'].count().sort_values(ascending=False) # descending sort count
print(df4)