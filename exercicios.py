'''
# Exercício 1

# Solicitando dois números
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Somando os dois números
soma = num1 + num2

# Exibindo o resultado
print("A soma dos dois números é:", soma)
'''
'''
# Exercício 2

# Solicitando um número
num = int(input("Digite um número: "))

# Verificando se o número é ímpar
impar = num % 2 == 0

# Exibindo o resultado
print(impar)
'''
'''
# Exercício 3

# Solicitando dois valores
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

# Verificando se num1 > 3 ou se num2 < 4 e exibindo
print(num1 > 3)
print(num2 < 4)
'''
'''
# Exercício 4

# Solicitando um número
num = complex(input("Digite um número: "))

# Alterando o valor de num para o seu módulo
num = abs(num)

# Exibindo o resultado
print("O módulo do número é:", num)
'''
'''
# Exercício 5

# Solicitando dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Verificando se são pares
num1par = num1%2 == 0
num2par = num2%2 == 0

# Exibindo o resultado
print("O primeiro número é par? ", num1par, ".O segundo número é par? ", num2par)
'''
'''
# Exercício 6

# Solicitando dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verificando se são negativos
num1neg = num1 < 0
num2neg = num2 < 0

# Exibindo o resultado
print("O primeiro número é negativo?", num1neg, ".O segundo número é negativo?", num2neg)
'''
'''
# Exercício 7

# Solicitando três valores
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calculando a média dos valores
media = (num1 + num2 + num3)/3

# Exibindo o resultado
print("A média entre os três números é:", media)
'''
'''
# Exercício 8

# Solicitando os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(num2 * 3 - 15)

# Verificando se num1 + 15 = num2 * 3
verificacao = num1 == num2 * 3 - 15

# Exibindo o resultado
print("O primeiro número mais quinze é igual ao triplo do segundo número?", verificacao)
'''
'''
# Exercício 9

# Solicitando dois números
num1 = float(input("Digite um numerador: "))
num2 = float(input("Digite um denominador: "))

# Realizando as operações
quociente = num1 / num2
resto = num1 % num2

# Exiibindo todas as informações:
print(num1, "  / ", num2, " = ", quociente, "| Resto:", resto)
'''
'''
# Exercício 10

# Solicitando a temperatra em graus Celsius
celsius = float(input("Digite a temperatura em ºC: "))

# Convertendo para graus Fahrenheit
fahrenheit = 9 * celsius / 5 + 32

# Exibindo o resultado
print("A temperatura digitada em graus Celsius equivale a", fahrenheit, "ºF.")
'''
'''
# Exercício 11

# Solicitando a massa e a altura do usuário
massa = float(input("Digite a sua massa, em kg: "))
altura = float(input("Digite a sua altura, em m: "))

# Calculando o IMC
imc = massa / altura ** 2

# Exibindo o resultado
print("%.2f" % imc)
'''
'''
# Exercício 12

# Solicitando três notas ao usuário
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))


# Solicitando os pesos das três notas
p1 = float(input("Digite o peso da primeira nota: "))
p2 = float(input("Digite o peso da segunda nota: "))
p3 = float(input("Digite o peso da terceira nota: "))

# Calculando a média ponderada das três notas
media = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)

# Exibindo o resultado
print(media)
'''
'''
# Exercício 13

# Solicitando a base e o expoente ao usuário
base = int(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

# Calculando a potência
potencia = base ** expoente

# Exibindo o resultado
print(potencia)
'''
'''
# DESAFIO 01

# Solicitando um número ao usuário
num = float(input("Digite um número: "))

# Calculando a raiz cúbica do número
raiz = num ** (1/3)

# Exibindo o resultado
print(raiz)
'''

# DESAFIO 02

# Solicitando as informações iniciais
capital = float(input("Digite o capital: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite o tempo, em anos: "))

# Calculando os juros compostos
montante = capital * (1 + taxa) ** tempo

# Exibindo o resultado
print("O montante é:", montante)