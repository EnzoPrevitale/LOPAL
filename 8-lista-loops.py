# 01 - Múltiplos de 3
'''
multiplos_tres = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 3 == 0:
        multiplos_tres += 1
print(f"Você digitou {multiplos_tres} múltiplos de 3.")
'''
# 02 - Senha
'''
senha = input("Defina a sua senha: ")

while True:
    tentativa = input("Digite a senha: ")
    if tentativa == senha:
        print("Acesso concedido!")
        break
'''
# 03 - Menu
'''
while True:
    print("Selecione uma opção: \n 1 - Iniciar \n 2 - Configurações \n 3 - Sair")
    opcao = int(input("Digite a sua opção: "))
    if opcao == 1:
        print("Iniciar")
    elif opcao == 2:
        print("Configurações")
    elif opcao == 3:
        print("Sair")
        break
    else:
        print("Opção inválida")
'''
# 04 - Primos
'''
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
multiplos = 0
primos = []

if num2 > num1:
    for j in range(num1, num2 + 1):
        for i in range(2, j):
            if j % i == 0:
                multiplos += 1
        if multiplos == 0 and j > 1:]
            # Primo
            primos.append(j)
        multiplos = 0
else:
    for j in range(num2, num1 + 1):
        for i in range(2, j):
            if j % i == 0:
                multiplos += 1
        if multiplos == 0 and j > 1:
            # Primo
            primos.append(j)
        multiplos = 0
print(primos)
'''
# 05 - Senha 3 tentativas
'''
tentativas = 0
senha = input("Defina a sua senha: ")
while tentativas < 3:
    tentativa = input("Digite a senha: ")
    if tentativa == senha:
        print("Acesso concedido.")
        break
    else:
        print("Tente novamente.")
    tentativas += 1
'''
# 06 - Par ou ímpar
'''
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Pares: {pares} \n Ímpares: {impares}")
'''
# 07 - Vogais
'''
frase = input("Digite uma frase: ")
vogais = 0

for char in frase:
    if char.upper() == 'A' or char.upper() == 'E' or char.upper() == 'I' or char.upper() == 'O' or char.upper() == 'U':
        vogais += 1
print(f"A frase tem {vogais} vogais.")
'''
# 08 - Cara ou coroa
'''
import random

espaco_amostral = ["Cara", "Coroa"]

evento = random.choice(espaco_amostral)

print(evento)
'''
# 09 - Abaixo da média
'''
sequencia = []
tamanho = int(input("Digite o tamanho da sequência: "))
soma = 0
abaixo_media = []

for i in range(tamanho):
    numero = float(input("Digite um item da sequência: "))
    soma += numero
    sequencia.append(numero)

media = soma / len(sequencia)

for i in sequencia:
    if i < media:
        abaixo_media.append(i)

print(f"{abaixo_media} estão abaixo da média.")
'''
# 10 - Segundo maior número
'''
sequencia = []
tamanho = int(input("Digite o tamanho da sequência: "))

for i in range(tamanho):
    numero = float(input("Digite um item da sequência: "))
    sequencia.append(numero)

for i in range(len(sequencia) - 2):
        sequencia.remove(min(sequencia))
        
segundo_menor = min(sequencia)

print(f"O segundo menor número da lista é {segundo_menor}.")
'''
# 11 - População de Coelhos
'''
num_inicial = int(input("Digite o número inicial de coelhos: "))

while num_inicial < 1:
    num_inicial = int(input("Digite o número inicial de coelhos: "))

taxa_reproducao = int(input("Digite a taxa de reprodução dos coelhos: "))

while taxa_reproducao < 1:
    taxa_reproducao = int(input("Digite a taxa de reprodução dos coelhos: "))

taxa_mortalidade = int(input("Digite a taxa de mortalidade dos coelhos: "))
while taxa_mortalidade < 0:
    taxa_mortalidade = int(input("Digite a taxa de mortalidade dos coelhos: "))

geracoes = int(input("Digite o número de gerações que deseja simular: "))
while geracoes < 1:
    geracoes = int(input("Digite o número de gerações que deseja simular: "))

populacao = num_inicial + (taxa_reproducao - taxa_mortalidade) ** geracoes

print(f"Em {geracoes} gerações, haverão {populacao} coelhos.")
'''
# 12 - Forca
import random

palavra = random.choice(["Python", "Java", "Assembly", "Pascal", "Cobol", "Fortran", "JavaScript", "Rust", "Ruby", ])

palavra_oculta = ("_ " * len(palavra)).split(" ")
erros = []

chances = 6

while True:
    exibir_palavra = "".join(palavra_oculta)
    exibir_erros = " ".join(erros)

    if exibir_palavra == palavra:
        print("Você venceu!")
        break
    elif chances <= 0:
        print("Você perdeu!")
        break

    print(f"{exibir_palavra} | {chances} chances | Erros: {exibir_erros}")

    palpite = input("Digite uma letra: ")
    while len(palpite) != 1:
        palpite = input("Digite uma letra: ")

    ocorrencias = 0
    for i in range(len(palavra)):
        if palpite.upper() == palavra[i].upper():
            palavra_oculta[i] = palpite.upper() if i == 0 else palpite.lower()
            ocorrencias += 1
    if ocorrencias == 0:
        chances -= 1
