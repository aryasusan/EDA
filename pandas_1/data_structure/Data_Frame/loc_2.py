import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/sample4.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','phno','location']

# questions:
# 1. age above 22- fname,lname,age,phno
# 2. age=21, fname,lname,age
# 3. chennai work- fname,lname,age,phno
# 4. age>23 and location=chennai - fname,lname,age

df1 = df.loc[df['age']>22] [['fname','lname','age','phno']]
print(df1)

df2 = df.loc[df['age']==21] [['fname','lname','age']]
print(df2)

df3 = df.loc[df['location']=='Chennai'] [['fname','lname','age','phno']]
print(df3)

df4 = df.loc[(df['location']=='Chennai')&(df['age']>23)] \
            [['fname','lname','age']]
print(df4)