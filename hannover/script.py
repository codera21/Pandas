import numpy as np
import pandas as pd

df = pd.read_csv("hannover.csv")
print(df.columns)
print(df.count())
df1 = df.drop_duplicates()
print(df1.count())
