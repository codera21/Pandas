import pandas as pd

file_name1 = input("Enter first file name: ")
file_name2 = input("Enter second file name: ")
on_value = input("Enter unique id column: ")

try:
    df1 = pd.read_excel(file_name1.strip())
    df2 = pd.read_excel(file_name2.strip())
except:
    df1 = pd.read_csv(file_name1.strip())
    df2 = pd.read_csv(file_name2.strip())


df = df2.merge(df1, indicator=True, on=[on_value], how='left')
print(df.head())
print(df.count())
df.to_csv("results.csv", index=False)
print("Script Completed, Please check results.csv for result set")
