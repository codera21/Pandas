import pandas as pd

df = pd.read_csv('doximity.csv', low_memory=False)
print(df.columns)
print(df.count())
df1 = df.drop_duplicates()
print(df1.count())
