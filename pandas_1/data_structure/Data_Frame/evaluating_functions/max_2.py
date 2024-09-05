import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/evaluating_functions/Temperature',sep=' ',header=None)
df.columns = ['year','temp']

df1 = df.groupby('year') ['temp'].max()\
        .sort_values(ascending=False)
print(df1)