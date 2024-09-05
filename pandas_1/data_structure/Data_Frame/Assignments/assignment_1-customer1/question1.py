import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','location']

#Question 1
print(df.shape[0])

#Question 2
df2 = df.drop_duplicates()
print(df2.shape[0])

#Question 3
df3 = df.sort_values(by='age',ascending=False) \
            [['fname','lname','prof','location']].head(10)
print(df3)

#Question 4
df4 = df.sort_values(by='age',ascending=False) \
            [['fname','lname','prof','location']].tail(5)
print(df4)

#Question 5
df5 = df.groupby('location') ['location'].count().sort_values(ascending=False)
print(df5)

#Question 6
df6 = df.loc[df['location']=='australia']
print(df6)

#Question 7
df7 = df.groupby('age') ['age'].count().sort_values(ascending=False)
print(df7)

#Question 8
df8 = df.groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df8)

#Question 9_A
df9_A = df.loc[df['location']=='india'].shape[0]
print(df9_A)

#Question 9_B
df9_B = df.loc[df['location']=='india'] \
        .groupby('prof') ['prof'].count() \
        .sort_values(ascending=False)
print(df9_B)

#Question 9_C
df9_C = df.loc[df['location']=='india']\
            .sort_values(by='age',ascending=False) \
            [['fname','lname','age','prof']].head(3)
print(df9_C)

#Question 9_D
df9_D = df.loc[df['location']=='india']\
            .sort_values(by='age',ascending=False) \
            [['fname','lname','age','prof']].tail(3)
print(df9_D)

#Question 9_E
df9_E = df.loc[(df['location']=='india')&(df['age']>40)]
print(df9_E)

#Question 9_F
df9_F = df.loc[(df['location']=='india')&(df['age']>30)&(df['age']<40)]
print(df9_F)

#Question 10_A
df10_A = df.loc[df['location']=='us'].shape[0]
print(df10_A)

#Question 10_B
df10_B = df.loc[df['location']=='us']\
            .groupby('age') ['age'].count()
print(df10_B)

#Question 10_C
df10_C = df.loc[df['location']=='us']\
            .groupby('prof') ['prof'].count()
print(df10_C)

#Question 10_D
df10_D = df.loc[(df['location']=='us')&(df['prof']=='Civil engineer')&(df['age']>30)]
print(df10_D)