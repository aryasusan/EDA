# combination of left and right outer joining

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

df3 = pd.merge(df1,df2,on='id',how='outer')
print(df3)