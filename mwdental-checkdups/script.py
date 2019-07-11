import pandas as pd

df = pd.read_excel("midwestdental.xlsx")
print(df.count())
df1 = df.drop_duplicates()
print(df1.count())
