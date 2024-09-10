import pandas as pd

df = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/missing_data.csv')
print(df)

print(df.columns)
print(df.isna().sum())
df.fillna(300,inplace=True) # replaces all missing with 300

# how to fill data using specific column

# calories column fill
df['Calories'].fillna(350,inplace=True)
df['Date'].fillna('2024/09/09',inplace=True)

#  if data is integer values use median or mode,
#  if float use mean,
#  if object use mode
# mode - most repeated value
mean_calories = df['Calories'].mean()
df['Calories'].fillna(mean_calories,inplace=True)
print(df)

mode_calories = df['Calories'].mode()[0]
df['Calories'].fillna(mode_calories,inplace=True)
print(df)

mode_date = df['Date'].mode()[0]
df['Date'].fillna(mode_date,inplace=True)
print(df)