import pandas as pd

df1 = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/results.unknown',sep=',',header=None)
df1.columns = ['roll_no','result']

df2 = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/student.unknown',sep=',',header=None)
df2.columns = ['name','roll_no']

df3 = pd.merge(df1,df2,on='roll_no',how='inner')

df4 = df3.loc[df3['result']=='pass']
print(df4)