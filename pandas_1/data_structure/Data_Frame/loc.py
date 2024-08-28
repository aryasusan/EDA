# loc works same like filter
# newdf = old_df.loc[old_df['column_name']condition]
#  if more than 1 condition:
#  newdf = old_df.loc[(old_df['column_name']condition)operator(old_df['column_name']condition)]

# query continuation to next line is indicated by \

import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']

df1 = df.loc[df['age']>50]
print(df1)

df2 = df.loc[df['country']=='india']
print(df2)

df3 = df.loc[df['prof']=='Doctor']
print(df3)

df4 = df.loc[df['age']<30]
print(df4)

# india location and their fname,age
df2 = df.loc[df['country']=='india'] [['fname','age']]
print(df2)

# india location age above 50
df2 = df.loc[(df['country']=='india')&(df['age']>50)]
print(df2)

# query continuation to next line is indicated by \
# india location and age above 50  and display their fname,age
df2 = df.loc[(df['country']=='india')&(df['age']>50)] \
            [['fname','age']]
print(df2)