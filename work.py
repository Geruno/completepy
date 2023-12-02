import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
uniqueValue = data['whoAmI'].unique()
oneHot = pd.DataFrame()
for value in uniqueValue:
    oneHot[value] = (data['whoAmI'] == value).astype(int)
oneHot.head()
print(oneHot)