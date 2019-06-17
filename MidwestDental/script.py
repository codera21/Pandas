import pandas as pd

df = pd.read_excel('midwestdental.xlsx')
print(df.columns)
df1 = df[df['Manufacturer'].isnull()]
# select only a few rows
df2  = df1[['SKU',  'Product Page URL']].head()
df2.to_csv('test_mfg.csv')

df1 = df[df['MFR Part #'].isnull()]
print(df1.count())
df1.to_csv('test_part_num.csv' , index=False)