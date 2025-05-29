import pandas as pd

df = pd.read_csv("arquivos/historico.csv")

df.to_json("arquivos/historico.json", indent=4)