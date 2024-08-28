import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']
print(df.isna().sum()) # no.of missing value in column
df1 = df.fillna('india') # fills with this value wherever the value is missing
print(df1)
print(df1.isna().sum())