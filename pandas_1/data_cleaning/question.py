import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/heart.csv')
print(df)

# Q1: print columns
for i in df:
    print(i)   # column names
print(df.columns)

# Q2 print datatypes
print(df.dtypes)

# Q3 target column count(desc)
df2 = df.groupby('target') ['target'].count().sort_values(ascending=False)
print(df2)

# Q4 separate x and y
# x= assign values except the last column to row and y= assign the last column to y using iloc
x = df.iloc[:,:-1]
print(x)
y = df.iloc[:,-1]
print(y)

# Q5 find total no of missing values
print(df.isna().sum()) # no.of missing value in column

# Q6 fill missing values using proper method
mean_trestbps = df['trestbps'].mean() # datatype is float so use mean
df['trestbps'].fillna(mean_trestbps,inplace=True)

print(df['restecg'].unique()) # displays value
mode_restecg = df['restecg'].mode()[0]
df['restecg'].fillna(mode_restecg,inplace=True)

print(df['thalach'].unique())
mean_thalach = df['thalach'].mean()
df['thalach'].fillna(mean_thalach,inplace=True)

mean_ca = df['ca'].mean()
df['ca'].fillna(mean_ca,inplace=True)

mean_thal = df['thal'].mean()
df['thal'].fillna(mean_thal,inplace=True)
print(df)

# Q7 consider thalach > 180 as wrong data and replace it with its mean
mean_value = df['thalach'].mean()
for i in df.index:
    if(df.loc[i,'thalach'] > 180):
        df.loc[i,'thalach'] = mean_value
print(df)