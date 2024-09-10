import pandas as pd

dic1 = {
            'id':[1,2,3,4,5],
            'fname':['arya','susan','babu','peter','heath'],
            'lname':['basil','babu','jacob','rheen','beena'],
            'age':[22,23,24,25,26]
        }
df1 = pd.DataFrame(dic1)

dic2 = {
            'id':[4,5,6,7,8],
            'prof':['ai','ml','ui','test','java'],
            'salary':[20,30,40,50,60],
            'location':['india','us','uk','india','aus']
        }
df2 = pd.DataFrame(dic2)

# id is the common column with common values as 4,5.
# so the values corresponding to 4 n 5 will be returned

df3 = pd.merge(df1,df2,on='id',how='inner')
print(df3)
#    id  fname  lname  age prof  salary location
# 0   4  peter  rheen   25   ai      20    india
# 1   5  heath  beena   26   ml      30       us

df5 = df3.loc[df3['age']>25]
print(df5)

df4 = pd.merge(df1,df2,on='id',how='inner') [['fname','age','prof']]
print(df4)
#    fname  age prof
# 0  peter   25   ai
# 1  heath   26   ml

