import pandas as pd 
df1 = pd.read_csv('Rover_1.csv')
df2 = pd.read_csv('Rover_2.csv')
df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df3.count())
df3 = df3.drop_duplicates()
print(df3.count()) 
