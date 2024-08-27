import pandas as pd

# NESTED LIST:
list1 = [
        [1,'arya','susan',31,'ds',20000],
        [2,'susan','babu',23,'py',2000],
        [3,'babu','jacob',36,'ai',50000],
        [4,'jacob','babu',25,'ml',6000],
        [5,'beena','varg',18,'ed',5000],
        [6,'basil','peter',28,'ds',40000],
        [7,'rheen','joy',37,'py',40000]
    ]

df = pd.DataFrame(list1)
print(df)

df = pd.DataFrame(list1,columns=['id','fname','lname','age','prof','salary'])
print(df)
print(df.shape)
print(df.dtypes) # datatype of each column and a highest datatype will be displayed

#NESTED DICTIONARY:
dic = {id:[1,2,3,4,5],'fname':['arya','susan','babu','jacob','beena'],'age':[31,23,36,25,18],'prof':['ds','ds','py','ml','ai']}
df = pd.DataFrame(dic) # key acts as column name
print(df)