import pandas as pd

df1 = pd.read_csv("xfinity_com.csv")
df = df1.sort_values('Period (Months)', ascending=False)
df = df.drop_duplicates(subset=['Address', 'Product', 'Product Name'])
df = df.sort_values('City')
print(df.groupby('City').size())
print(df.groupby('Product').size())
df.to_csv("xfinity_deduped.csv", index=False)
