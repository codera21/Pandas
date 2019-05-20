import pandas as pd

df = pd.read_csv('mw.csv')
# print(df.columns)
print("SKU Count before ", df['SKU'].count())
df1 = df.drop_duplicates(subset=['SKU'])
print("SKU Count After dedupe ", df['SKU'].count())
