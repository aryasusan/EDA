# sort based on a column

import pandas as pd

df = pd.read_csv('/pandas_1/data_structure/Data_Frame/file_convertion/sample4.txt', sep=',', header=None)
df.columns = ['Id','fname','lname','age','phno','location']

df1 = df.sort_values(by='age') #ascending based on age
df2 = df.sort_values(by='fname',ascending=False) #descending basd on fname

print(df1)
print(df2)


