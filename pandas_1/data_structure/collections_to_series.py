import pandas as pd

a = pd.Series([1,2,3,4,5]) # list to series, index from 0 to n-1
print(a)
print(a.dtype)
print(a.ndim)
print(a.shape)

b = pd.Series((1,2,3,4,5)) # tuple to series , index from 0 to n-1
print(b)

c = pd.Series({1:'Arya',2:'Susan',3:'babu'}) # dictionary to series, key acts as index
print(c)
