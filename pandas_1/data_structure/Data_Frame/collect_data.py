import pandas as pd

l1 = [
        [1,'arya','susan',31,'ds',20000],
        [2,'susan','babu',23,'py',2000],
        [3,'babu','jacob',36,'ai',50000],
        [4,'jacob','babu',25,'ml',6000],
        [5,'beena','varg',18,'ed',5000],
        [6,'basil','peter',28,'ds',40000],
        [7,'rheen','joy',37,'py',40000]
    ]
df = pd.DataFrame(l1,columns=['id','fname','lname','age','prof','salary'])

# first 4 employees' fname,lname,age,prof
df_rows = df.head(10)
df_new = df_rows[['fname','lname','age','prof']]
print(df_new)

# single line implementation: pick required columns first and then required rows
df_new = df[['fname','lname','age','prof']].head(4)
print(df_new)

# last 3 employees' fname,age,prof,salary
df_new = df[['fname','age','prof','salary']].tail(3)
print(df_new)