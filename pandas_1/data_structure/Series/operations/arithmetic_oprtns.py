import pandas as pd

s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series([6,8,9,5,4])

s3 = s1.add(s2)
print(s3) # NaN will be shown in the corresponding index if the order is not same

s4 = s1.sub(s2)
print(s4)

s5 = s1.multiply(s2)
print(s5)

s6 = s1.div(s2)
print(s6)