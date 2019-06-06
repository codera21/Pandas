import pandas as pd 

df  = pd.read_csv('NSR_Cable_Pricing_Analysis - Data.csv')
df1 = df.loc[df['Website'] == 'https://www.spectrum.com/internet.html']
df.to_csv('Spectrum.csv' , index=False)