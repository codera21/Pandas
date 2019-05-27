import pandas as pd
df1 = pd.read_csv('benco_1.csv', low_memory=False)
df2 = pd.read_csv('benco_2.csv', low_memory=False)
df = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df.count())
df = df.drop_duplicates(subset=['SKU'])
print(df.count()) 
df.to_csv('benco_may.csv', index=False)