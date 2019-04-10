import numpy as np
import pandas as pd

df = pd.read_csv("motocard.csv")
print(df.columns)
null_idx = df['RETAIL PRICE'].isnull()
df.loc[null_idx, 'RETAIL PRICE'] = df['SALE PRICE']
df.loc[null_idx, 'SALE PRICE'] = np.nan
print(df.count())
df.to_csv("motocard_fix.csv", index=False)