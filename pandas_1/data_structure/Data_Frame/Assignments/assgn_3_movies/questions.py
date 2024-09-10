import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/movies_cleaned_pandas.csv',sep=',',header=None)
df.columns = ['id','name','year','rating','duration']

#Question 1
print(df.shape[0])

#Question 2
df2 = df.drop_duplicates()
print(df2.shape[0])

#Question 3
df3 = df.sort_values(by='year',ascending=False)
print(df3)

#Question 4
df4 = df.sort_values(by='rating',ascending=False) \
            [['name','year','rating']].head(5)
print(df4)

#Question 5
df5 = df.sort_values(by='rating',ascending=False) \
            [['name','year','rating']].tail(5)
print(df5)

#Question 6
df6 = df.groupby('year') ['year'].count().sort_values(ascending=False)
print(df6)

#Question 7
df7 = df.groupby('rating') ['rating'].count().sort_values(ascending=False)
print(df7)

#Question 8
df8 = df.loc[(df['year']==2008)&(df['rating']>3)]
print(df8)

#Question 9
df9= df.sort_values(by='duration',ascending=False) \
            [['name','year','rating','duration']].head(1)
print(df9)

#Question 10
df10= df.sort_values(by='rating') \
            [['name','year','rating','duration']].head(1)
print(df10)

#Question 11A
df11A= df.loc[(df['year']==2005)&(df['rating']>4)] \
         .sort_values(by='rating').tail(1)
print(df11A)

#Question 11B
df11B= df.loc[(df['year']==2005)&(df['rating']>4)] \
         .sort_values(by='rating').head(1)
print(df11B)

#Question 12
df12 = df.loc[df['year']==2008] \
         .groupby('year') ['year'].count()
print('*'*100)
print(df12)
print('*'*100)

#Question 13
df13 = df.loc[(df['year']>1975)&(df['year']<2000)]
print(df13.shape[0])

#Question 14
df14 = df.loc[(df['year']>1975)&(df['year']<2000)&(df['rating']>3.5)]
print(df14.shape[0])