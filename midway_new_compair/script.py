import pandas as pd

df1 = pd.read_excel('nash-new.xlsx')
df2 = pd.read_excel('nash-old.xlsx')

df = df2.merge(df1, on=['SKU', 'Product Page URL'], indicator=True , how='left')
df = df[['SKU', 'Product Page URL','_merge']]
print(df.head())
df.to_csv("missing.csv", index=False)
