import pandas as pd

df = pd.read_excel("arquivos/historico.xlsx")

df.to_csv("arquivos/historico.csv")