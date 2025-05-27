'''
.txt
    Texto simples
.csv
    Nome,Idade,Profissão
    João,25,Engenheiro
    Maria,30,Médica
.json
    {
    "nome":"João",
    "idade":25,
    "profissão":"Engenheiro"
    }
.xml
    <pessoa>
        <nome>João</nome>
        <idade>25</idade>
        <profissão>Engenheiro</profissão>
    </pessoa>
.xlsx
    _______________
   | Nome | Idade |
   |______________|
   | João |    25 |
   |______________|
   | Maria|    30 |
   |______________|
'''
'''
# .txt

with open("text.txt", "w") as file:
    file.write("Olá, mundo!\n")
    file.write("Python é divertido!\n")

with open("text.txt", "r") as file:
    print(file.read())
'''
'''
# .csv

import csv
with open("produtos.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "preço"])
    writer.writerow(["livro", 20])

with open("produtos.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''
'''
# .json
import json

with open("dados.json", "w", encoding="utf-8") as file:
    json.dump({"nome": "João", "idade": 25}, file, indent=4)

with open("dados.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)
'''
'''
# XML
with open("config.xml", "w", encoding="utf=8") as file:
    file.write("""<?xml version="1.0" encoding="UTF-8"?>
<config>
    <versão>1.0</versão>
</config>""")

with open ("config.xml", "r", encoding="utf-8") as file:
    print(file.read())
'''
import pandas as pd

data = pd.DataFrame({"Produto": ["Celular"],
                     "Quantidade": 10})

data.to_excel("vendas.xlsx", index=False)

sheet = pd.read_excel("vendas.xlsx")
print(sheet.head())