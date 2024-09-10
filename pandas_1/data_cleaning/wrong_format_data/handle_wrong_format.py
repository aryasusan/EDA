#  date in 26th index is in wrong format

import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/missing_data.csv')
print(df)

# df['Date'] = pd.to_datetime(df['Date'])
# print(df)

# will be covered in ML