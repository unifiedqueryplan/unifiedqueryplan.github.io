import pandas as pd
pd.set_option('display.max_rows', None)

df = pd.read_csv('data.csv', header=None)
df.columns = ['category','query','target','count']


print(" Mean:")
print(df.groupby(['category', 'target']).mean())

print(" Variance by each query and operation category:")
print(df.groupby(['category', 'query']).var(numeric_only=True))