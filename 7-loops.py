### FOR ###
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
'''
# Criando uma lista vazia
lista = []
# Solicitando o tamanho da lista ao usuário
tamanho = int(input("Digite o tamanho da sua lista: "))

# Declarando a variável soma
soma = 0

# Percorrendo a lista
for i in range(1, tamanho + 1):
    # Solicitando os valores da lista
    numero = float(input("Digite um número: "))

    # Adicionando os valores à lista
    lista.append(numero)

    # Adicionando o valor à somatória total
    soma += numero

    # Imprimindo a lista
    print(lista)

# Calculando a média utilizando a fórmula da soma dos termos de uma PA para calcular a somatória dos termos
media =  soma / tamanho

# Imprimindo a lista, o tamanho e a média
print(f"A média dos valores da lista {lista}, de tamanho {tamanho}, é {media}.")
'''

### TESTE DE MESA ###
'''
a = 2
b = 3
for i in range(2):
    a = a + b
    b = b - 1
print(a,b)
'''
'''
-------
|A|B|i|
|2|3|0|
|5|2|1|
|7|1| |
-------
'''
'''
x = 1
y = 2
z = 0
for i in range(3):
    z = z + x
    x = x + y
print(x, y, z)
'''
'''
---------
|x|y|z|i|
|1|2|0|0|
|3|2|1|1|
|5|2|4|2|
|7|2|9| |
---------
'''

### WHILE ###
'''
x = 0

while x < 10:
    x += 1
    print(x)
'''

### TESTE DE MESA ###
'''
m = 5
n = 1
while m > 2:
    n = n + 2
    m = m - 1
print(m, n)
'''
'''
-----
|m|n|print(m, n)
|5|1|   2 7
|4|3|
|3|5|
|2|7|
-----
'''

'''
|x|y|z|print(x, y, z)
|3|4|0|
|4| |3|
||||
'''

# 01
'''
# Solicitando um número
num = int(input("Digite um número de 5 a 10: "))

# Verificando se o número digitado está no intervalo especificado
if 5 <= num <= 10:
    # Imprimindo o valor inicial
    print(num)

    # Rodando um loop para fazer a contagem regressiva
    while num != 0:
        # Subtraindo o número inicial em uma unidade
        num -= 1

        # Imprimindo cada valor da contagem regressiva
        print(num)
# O número não está no intervalo especificado
else:
    # Exibindo uma mensagem avisando que o número não está no intervalo especificado
    print("O número não se encontra no intervalo especificado.")
'''
# 02 - Maior entre cinco
'''
num = 0

# Solicitando 5 números ao usuário
quantidade_num = 0
while quantidade_num < 5:
    quantidade_num += 1
    temp = num
    num = float(input(f"Digite um número ({quantidade_num}): "))

    if temp > num:
        num = temp
print(f"O maior número digitado é {num}")
'''
# 03 - Fatorial
'''
num = int(input("Digite um número: "))
contador = num
if num > 0:
    while contador != 1:
        contador -= 1
        num = num * contador
    print(f"O fatorial é: {num}.")
elif num < 0:
    print("A função fatorial não está definida para qualquer n < 0.")
else:
    num = 1
    print(f"O fatorial é: {num}.")
'''
# 04 - Média de lista com tamanho escolhido pelo usuário
'''
lista = []
tamanho = int(input("Digite o tamanho da lista: "))
contador = 0
soma = 0

while contador < tamanho:
    contador += 1
    num = float(input("Digite um item da lista: "))
    lista.append(num)
    soma = soma + num
media = soma / tamanho
print(media)
'''
# 05 - Calculadora com Menu
opcao = ""
num1, num2 = 0, 0
resultado = 0

while opcao != "SAIR":
    opcao = input("Digite a sua opção: \n (+) - Soma \n (-) - Subtração \n (*) - Multiplicação \n (/) - Divisão \n (Sair) \n").upper()
    if opcao != "SAIR":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if opcao == "+":
            resultado = num1 + num2
        elif opcao == "-":
            resultado = num1 - num2
        elif opcao == "*":
            resultado = num1 * num2
        elif opcao == "/":
            resultado = num1 / num2

        print(f"O resultado é: {resultado}.")