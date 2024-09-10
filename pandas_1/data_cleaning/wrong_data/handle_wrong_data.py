# height        weight
# 350               50
# 150               48
# 160               70
# 155               450

# here height 350 and weight 450 is considered wrong data

import pandas as pd

df1 = pd.read_csv('/home/arya/EDAProjects/EDA_Project/files/missing_data.csv')
print(df1)

# 7th index -duration column element is wrong data
df1.loc[7,'Duration'] = 45
# print(df1)

# suppose it is impossible to find the wrong data from a big file. In that case we pass conditions
# eg, replace values of calories > 400 with its mean
mean_value = df1['Calories'].mean()
for i in df1.index:
    if(df1.loc[i,'Calories'] > 400):
        df1.loc[i,'Calories'] = mean_value
print(df1)