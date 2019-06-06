import pandas as pd 

df  = pd.read_csv('NSR_Cable_Pricing_Analysis - Data.csv')
print(df.columns)
print(df.count())
df1 = df.loc[df['website'] == 'https://www.spectrum.com/internet.html']
print(df1.count())