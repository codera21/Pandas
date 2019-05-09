import pandas as pd 
# df1 = pd.read_csv('atlanta.csv', low_memory=False)
# df2 = pd.read_csv('atlanta_old.csv', low_memory=False)

# df = df2.merge(df1, on=['SKU'], how='left', indicator=True)
# df_final = df.loc[df['_merge'] == 'left_only']
# df_final.to_csv('atlanta_final.csv', index= False)

df1 = pd.read_csv('atlanta_2019-04-29.csv' , low_memory=False)
df = df1.drop_duplicates(subset=['SKU'])
df.to_csv('atlanta_dedupe_2019-4-29.csv', index=False)