import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']

df1 = df.groupby('prof') ['prof'].count().sort_values(ascending=False) # descending sort count
print(df1)

#india work, each prof count
df2 = (df.loc[df['country']=='india'] \
        .groupby('prof') ['prof'].count() \
        .sort_values(ascending=False))
print(df2)