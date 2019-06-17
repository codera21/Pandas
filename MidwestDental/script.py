import pandas as pd

df = pd.read_excel('midwestdental.xlsx')
print(df.columns)
df1 = df[df['Manufacturer'].isnull()]
print(df1[['SKU',  'Product Page URL']].head())
df2  = df1[['SKU',  'Product Page URL']].head()
df2.to_csv('test.csv')