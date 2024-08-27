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

print(df.head(3),'first three row')
print(df.tail(2),'last 2 rows')