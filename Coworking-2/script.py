import pandas as pd
df = pd.read_csv('coworker.csv', low_memory=False)

for i, row in df.iterrows():
    print("processing row " , i)
    temp = df.loc[i, 'Address']
    temp = temp.split(',')
    temp = temp[-1]
    df.loc[i, 'Country'] = temp

df.to_csv('coworker-country_fix.csv' , index= False)