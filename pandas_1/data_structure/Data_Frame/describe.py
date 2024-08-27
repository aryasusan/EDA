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
df = pd.DataFrame(list1,columns=['id','fname','lname','age','prof','salary'])
print(df.describe()) # describes the numerical columns

print(df.describe(include='O'))  # describes the object columns
# unique- count of unique elements,
# top describes the most repetitive element, if not repeating, takes the 1st element, if multiple element has same repeat count-takes the first element
# freq- count of top

print(df.describe(include='all')) # includes both numerical and object column