# head is used to collect first 5 elements in the series by default
# in case of data frame it will be first 5 rows
# to collect particular number of elements, pass it in head

# tail is used to collect tailing members, default 5

import pandas as pd

a = pd.Series([3,4,5,67,2,1,50,43,100,64,71,12,1])
print(a.head())
print(a.head(7))

print(a.tail())
print(a.tail(3))