import pandas as pd 
df1 = pd.read_csv('Nashvilledental-new.csv')
df2 = pd.read_csv('Nashvilledental-old.csv')

df = df2.merge(df1, on=['SKU'], how='left', indicator=True)
# df.to_csv('nash_final.csv')
df_final = df.loc[df['_merge'] == 'left_only']
df_final.to_csv('nashville_final.csv', index= False)