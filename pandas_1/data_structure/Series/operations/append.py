import pandas as pd

s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series([6,8,9,5,4])

s3 = s1._append(s2)
print(s3) # index will not be correct
s4 = s1._append(s2,ignore_index=True)
print(s4) # index will be ordered