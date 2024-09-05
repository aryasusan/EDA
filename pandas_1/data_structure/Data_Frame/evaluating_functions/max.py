# max is used to find the max of a column based on each field of another column
# for eg, max age of each profession

# new_df = old_df.groupby('col_name') ['max_col_name'].max()

import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/pandas_1/data_structure/Data_Frame/file_convertion/customer1.txt',sep=',',header=None)
df.columns = ['Id','fname','lname','age','prof','country']

df1 = df.groupby('prof') ['age'].max() # max age corresponding to each profession
print(df1)

df2 = df.groupby('prof') ['age'].max().sort_values(ascending=False) # desc sort max age corresponding to each profession
print(df2)