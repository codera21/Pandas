import pandas as pd

df1 = pd.read_excel('nash-new.xlsx')
df2 = pd.read_excel('nash-old.xlsx')

df = df2.merge(df1, on=['SKU'], indicator=True , how='left')
df = df[['SKU', '_merge']]
print(df.head())
df.to_csv("missing.csv", index=False)
