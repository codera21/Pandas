import pandas as pd

df1 = pd.read_csv('1.csv')
df2 = pd.read_csv('2.csv')
df3 = pd.read_csv('3.csv')

df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(df.count())
df = df.drop_duplicates()
print(df.count()) 
df.to_csv('hdd_final.csv', index=False)