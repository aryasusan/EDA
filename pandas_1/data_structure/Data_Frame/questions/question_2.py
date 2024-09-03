# customer 1

# find the tot no of missing value,fill with india and then:
#     1. india work--fname,lname,age,prof
#     2. age max 5 employee--fname,lname,age,prof
#     3. age min 3 emloyee--fname,lname,age,prof
#     4. location uk, fname,lname,age
#     5. age betweeen 40-60 fname,lname,age,prof
#     6. india work-age max -2 employye- fname lname age
#     7. india and prof doc--fname,lname,age
#     8. pilot,age min -1 employee, fname,lname,age
#     9. actor, age max 2 employye-fname,lname,age
import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']

print(df.isna().sum())
df1 = df.fillna('india')

df2 = df1.loc[df['country']=='india'] [['fname','lname','age','prof']]
print(df2)
print('*'*50)

df3 = df1.sort_values(by='age',ascending=False) \
            [['fname','lname','age','prof']].head(5)
print(df3)
print('*'*50)

df4 = df1.sort_values(by='age',ascending=False) \
            [['fname','lname','age','prof']].tail(3)
print(df4)
print('*'*50)

df5 = df1.loc[df['country']=='uk'] [['fname','lname','age']]
print(df5)
print('*'*50)

df6 = df1.loc[(df['age']>40)&(df['age']<60)] [['fname','lname','age','prof']]
print(df6)
print('*'*50)

df7 = df1.loc[df['country']=='india'].sort_values(by='age',ascending=False) \
            [['fname','lname','age']].head(2)
print(df7)
print('*'*50)

df7 = df1.loc[(df['country']=='india')&(df['prof']=='Doctor')] \
            [['fname','lname','age']]
print(df7)
print('*'*50)

df8 = df1.loc[df['prof']=='Pilot'].sort_values(by='age',ascending=False) \
            [['fname','lname','age']].tail(1)
print(df8)
print('*'*50)

df8 = df1.loc[df['prof']=='Actor'].sort_values(by='age',ascending=False) \
            [['fname','lname','age']].head(2)
print(df8)
print('*'*50)


