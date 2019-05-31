import pandas as pd
import numpy as np
i = 0
chunksize = 10000
df = pd.read_excel('coworker_country_fix.xlsx')
for chunk in np.array_split(df, len(df) // chunksize):
    chunk.to_excel('coworker_{:02d}.xlsx'.format(i), index=False)
    i+=1
