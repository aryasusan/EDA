import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/Assignments/assgn_2_txn/txn.txt',sep=',',header=None)
df.columns = ['order_Id','purchase_date','custo_id','amount','product','category','city','state','payment_method']

#Question 1
print(df.shape[0])

#Question 2
df2 =df.loc[(df['purchase_date']>='01-01-2011') & \
            (df['purchase_date']<='01-31-2011')] \
            [['order_Id','custo_id','category','product','state']]
print(df2.shape[0])

#Question 3
df3 =df.loc[(df['purchase_date']>='07-01-2011') & \
            (df['purchase_date']<='07-31-2011')] \
            [['order_Id','custo_id','category','product','state']]
print(df3.shape[0])

#Question 4
df4 = df.groupby('category') ['category'].count().sort_values(ascending=False)
print(df4)

#Question 5
df5 = df.loc[df['category']=='Cardio Machine Accessories']
print(df5)

#Question 6
df6 = df.groupby('payment_method') ['payment_method'].count()
print(df6)

#Question 7
df7 =df.loc[(df['purchase_date']>='01-01-2011') & \
            (df['purchase_date']<='07-31-2011')] \
        .groupby('purchase_date') ['purchase_date'].count()
print(df7)

# Question 8
df8 = df.groupby('category') ['amount'].sum()
print(df8)

# Question 9
df9 = df.groupby('category') ['amount'].max()
print(df9)

# Question 10
df10 = df.groupby('category') ['amount'].mean()
print(df10)

# Question 11
df11 = df.groupby('payment_method') ['amount'].sum()
print(df11)

# Question 12
df12 = df.loc[df['product']=='Indoor Games']\
         .groupby('product') ['amount'].sum()
print(df12)

# Question 13
df13 = df.groupby('state') ['state'].count()
print(df13)


