# default separation is ',', if header(column names) is not present None shud be given
# else first row will be considered as column names

import pandas as pd

df = pd.read_csv('customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']
# print(df)
# print(df.shape)
# print(df.head(3))
# print(df.tail(2))
# print(df.dtypes)
# print(df[['fname','prof','country']])

# first 10 employees' fname,lname,age,prof
df_rows = df.head(10)
df_new = df_rows[['fname','lname','age','prof']]
# print(df_new)
# single line implementation: pick required columns first and then required rows
df_new = df[['fname','lname','age','prof']].head(10)
# print(df_new)

# last 50 employees' fname,age,prof,country
df_new = df[['fname','age','prof','country']].tail(50)
print(df_new)


df = pd.read_csv('customer5.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country','salary']
# print(df)
