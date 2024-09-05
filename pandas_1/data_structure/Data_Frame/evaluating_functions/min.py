import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']

df1 = df.groupby('prof') ['age'].min() # min age corresponding to each profession
print(df1)

# ------------------------------------------------------------

df2 = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/evaluating_functions/Temperature',sep=' ',header=None)
df2.columns = ['year','temp']

df3 = df2.groupby('year') ['temp'].min()\
         .sort_values(ascending=False)
print(df3)