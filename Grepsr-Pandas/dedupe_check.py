import pandas as pd

filename = input("Enter file name: ")
try:
    df1 = pd.read_excel(filename.strip())
except:
    df1 = pd.read_csv(filename.strip())


print(df1.count())
print("=============== after dedudped =======================\n")
df = df1.drop_duplicates()
print(df.count())
print("\n Script Completed !! \n")
