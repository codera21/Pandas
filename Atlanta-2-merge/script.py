import pandas as pd 
df1 = pd.read_csv('atl1.csv')
df2 = pd.read_csv('atl2.csv')

df = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df.count())
df = df.drop_duplicates()
print(df.count()) 

df.to_csv('atlanta_may.csv', index=False)