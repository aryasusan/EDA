import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/missing_data.csv')
print(df)

df.dropna(inplace = True)
print(df)

df.dropna(inplace=True, ignore_index=True) #index correction
print(df)

df.dropna(subset=['Date'],inplace=True) # row with missing value in date is dropped
print(df)