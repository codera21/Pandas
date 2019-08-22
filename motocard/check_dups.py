import numpy as np
import pandas as pd

df = pd.read_excel("m.xlsx")
print(df.columns)
df = df.drop_duplicates(subset=['SKU'])
df.to_csv('final.csv', index=False)



