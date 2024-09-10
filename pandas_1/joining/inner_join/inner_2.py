import pandas as pd

df1 = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/order.txt',sep=',',header=None)
df1.columns = ['order_id','date','id','amount']

df2 = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/custom.txt',sep=',',header=None)
df2.columns = ['id','fname','age','location','salary']

df3 = pd.merge(df1,df2,on='id',how='inner') [['fname','age','location','salary','date','amount']]
print(df3)

# salary>2000 - name,age,location,date
df4 = df3.loc[df3['salary']>2000] [['fname','age','location','date']]
print(df4)

#pick employee with latest date and display name,age,salary,date
df5 = df3.sort_values(by='date',ascending=False) [['fname','age','salary','date']].head(1)
print(df5)

#max_age - name,age,date,amount
df6 = df3.sort_values(by='age',ascending=False) [['fname','age','date','amount']].head(1)
print(df6)