import pandas as pd
csv_path = "D://Desktop/SacramentocrimeJanuary2006.csv"
df = pd.read_csv(csv_path)
print(df.head())
x = df[["address"]]
print(x)