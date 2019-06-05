import pandas as pd

df1 = pd.read_csv('mayoclinic.csv')
df2 = pd.read_csv('mayoclinic.csv')

df = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df['ID'].count())
df = df.drop_duplicates(subset=['ID'])
print(df['ID'].count()) 
df.to_csv('mayoclinic_final.csv', index=False)