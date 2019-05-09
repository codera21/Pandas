import pandas as pd 
df1 = pd.read_csv('old.csv', low_memory=False)
df2 = pd.read_csv('new.csv', low_memory=False)

df = pd.concat([df1 , df2])
print(df.count())
df = df.drop_duplicates()
print(df.count())
df.to_csv('henryschein.csv', index=False)