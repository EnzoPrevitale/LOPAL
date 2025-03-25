'''
# Listas
frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)
'''

'''
# Strings
texto = "Hello World!"

for caractere in texto:
    print(caractere)
'''

'''
# Tuplas
cores = ("Vermelho", "Verde", "Azul")

for cor in cores:
    print(cor)
'''

'''
# Dicionários
pessoa = {
    "Nome": "Enzo",
    "Idade": 17,
    "Profissão": "Aprendiz DS"
}

print(pessoa["Nome"])
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
'''

'''
# Dicionários dentro de dicionários
alunos = {
    "23209": {
        "nome": "Enzo",
        "idade": 17
    },

    "22222": {
        "nome": "aaaa",
        "idade": 69
    }
}

for ra, dados in alunos.items():
    print(f"RA: {ra}")
    for chave, valor in dados.items():
        print(f" {chave.capitalize()}: {valor}")
'''

'''
# Conjuntos
animais = {"Gato", "Cachorro", "Elefante", "Girafa"}
for animal in animais:
    print("Animal:", animal)
'''

'''
# Range
for numero in range(100):
    print(2 ** numero)
'''

'''
# Arquivos
nome_arquivo = "teste/teste.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if linha.strip() == "teste":
            print("Hello world!")
'''

# 01
'''
# Percorrendo os números pares de 0 a 10
for i in range(0, 11, 2):
    # Imprimindo os números
    print(i)
'''
# 02
'''
# Declarando uma lista de cores
cores = ["Vermelho", "Azul", "Verde", "Amarelo"]

# Percorrendo a lista
for cor in cores:
    # Imprimindo a cor
    print(cor)
'''
# 03
'''
# Declarando x com valor 0
x = 0

# Percorrendo os números inteiros de 0 a 100
for i in range(101):
    # Somando todos os termos
    x = x + i

# Imprimindo o resultado
print(f"A soma de todos os números inteiros entre 1 e 100 é {x}.")
'''
# 04
'''
# Solicitando um número ao usuário
num = int(input("Digite um número: "))

# Percorrendo os inteiros de 1 a 10
for i in range(11):
    # Multiplicando num por i para obter o produto desejado
    produto = num * i
    # Imprimindo cada produto da tabuada
    print(f"{num} x {i} = {produto}")
'''
# 05

# Criando uma lista vazia
lista = []
# Solicitando o tamanho da lista ao usuário
tamanho = int(input("Digite o tamanho da sua lista: "))

# Percorrendo a lista
for i in range(1, tamanho + 1):
    # Solicitando os valores da lista
    lista.append(int(input("Digite um número: ")))
    # Imprimindo a lista
    print(lista)

# Calculando a média utilizando a fórmula da soma dos termos de uma PA para calcular a somatória dos termos
media = ((lista[0] + lista[tamanho - 1]) * (len(lista) / 2)) / tamanho

# Imprimindo a lista
print(media)