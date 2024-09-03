# hierarchy= loc-->sort-->columns_collect-->head/tail

# sample 4
# 1.age max -2 employee-fname,lname,age,ph
# 2.age min -1 employee--fname,lname,age,ph
# 3.chennai location -age max--- fname,lname,age,ph

import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/sample4.txt', sep=',', header=None)
df.columns = ['Id','fname','lname','age','phno','location']

df1 = df.sort_values(by='age',ascending=False) [['fname','lname','age','phno']].head(2)
print(df1)
print('*'*50)

df2 = df.sort_values(by='age') [['fname','lname','age','phno']].head(1)
print(df2)
print('*'*50)

df3 = df.loc[df['location']=='Chennai'].sort_values(by='age') [['fname','lname','age','phno']].tail(1)
print(df3)
print('*'*50)

