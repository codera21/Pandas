import pandas as pd

df1 = pd.read_csv('midway_new.csv')
df2 = pd.read_csv('midway_old.csv')

df = df2.merge(df1, on=['SKU', 'ProductPageURL'], indicator=True , how='left')
df = df[['SKU', 'ProductPageURL','_merge']]
print(df.head())
df.to_csv("missing.csv", index=False)
