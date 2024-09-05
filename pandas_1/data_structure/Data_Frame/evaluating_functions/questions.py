import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/evaluating_functions/customer5.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','location','salary']
# df2.columns = ['year','temp']

df1 = df.groupby('prof') ['prof'].count()\
         .sort_values(ascending=False)
print(df1)

df2 = df.groupby('prof') ['age'].max()\
         .sort_values(ascending=False)
print(df2)

df3 = df.groupby('location') ['salary'].sum()
print(df3)

df4 = df.groupby('prof') ['salary'].min()
print(df4)

df5 = df.groupby('age') ['salary'].max()
print(df5)

df6 = df.groupby('prof') ['salary'].max()
print(df6)