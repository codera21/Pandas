import pandas as pd

df = pd.read_csv('doximity.csv', low_memory=False)
df1 = df.loc[df['Specialty'] == 'Emergency Medicine']
print(df1.count())
print(df1.head())
df1.to_csv('doximity_emergency.csv' , index=False)