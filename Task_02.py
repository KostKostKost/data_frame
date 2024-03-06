import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = pd.Categorical(data['whoAmI'])
one_hot_encoded = pd.get_dummies(categories, prefix='whoAmI')

result = pd.concat([data, one_hot_encoded], axis=1)

result = result.drop('whoAmI', axis=1)

result.head()