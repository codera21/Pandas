import pandas as pd

df = pd.read_csv('mw.csv')
print(df.columns)
print(df.count())
df1 = df.drop_duplicates(subset=['SKU'])
print(df1.count())