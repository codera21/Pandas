import pandas as pd

df = pd.read_excel('purelyf.xlsx')
print(df.columns)
df1 = df[df['MFRPart #'].isnull()]
df2 = df1[['SKU',  'ProductPageURL']]
df2 = df2.drop_duplicates(subset="ProductPageURL")
df2.to_csv('test_mrfpart.csv')


