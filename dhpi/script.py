import pandas as pd

df = pd.read_csv('dhpionline.csv')
print(df.columns)
print("SKU Count before ", df['SKU'].count())
df1 = df.drop_duplicates()
print("SKU Count After dedupe ", df['SKU'].count())
