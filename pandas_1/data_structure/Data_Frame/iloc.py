# head and tail can collect either from starting or ending rows,
# to collect in between rows or any particular row,we use iloc where an index will be passed

import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']

df1 = df.iloc[4] # picks 5th row whose index is 4
# print(df1)

df1 = df.iloc[4:11] ##picks from 5th row to 10th row
# print(df1)

df1 = df.iloc[4:11] ##picks from 4th index to 10th index (5th row to 11th row)
# print(df1)

df1 = df.iloc[5:51:2] #[start: stop: step] index - 5,7,9...49
print(df1)

df1 = df.iloc[5:16,:3] #[row slice,column slice] row index: 5 to 15 column index:0 to 2
print(df1)

# assign values except the last column to row and assign the last column to y using iloc
x = df.iloc[:,:-1]
print(x)
y = df.iloc[:,-1]
print(y)