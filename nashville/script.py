import pandas as pd 
df1 = pd.read_csv('nash.csv')
print(df1.count())
df = df1.drop_duplicates()
print(df.count())
