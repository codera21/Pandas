import pandas as pd

df = pd.read_csv("Spectrum.csv")
print(df.columns)
df = df.drop_duplicates(subset=['Market Name', 'Company', 'Competitor',
                                'Telco Technology', 'Address', ])
print(df.count())
df.to_csv("spectrum_unique_addr.csv", index=False)
