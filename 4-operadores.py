'''
a = 8
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto_divisao = a % b
potenciacao = a ** b
'''
"""
#Exercicio 01

# Declarando as variaveis
x = float(input("Digite um número x: "))
y = float(input("Digite um número y: "))
z = float(input("Digite um número z: "))

# Utulizando as operações para calcular as médias
media = (x+y+z)/3
media_geometrica = (x*y*z)**(1/3)

# Imprimindo as médias
print("Média aritmética: ", media)
print("Média geométrica: ", media_geometrica)
"""

'''
# Exercício 2

# Solicitando o valor do capital
capital = float(input("Digite o valor da prestação: "))
taxa_de_juros = float(input("Digite a taxa de juros simples, em porcentagem: ")) / 100

# Calculando 110% (capital + 10% do valor) do capital
montante = capital * taxa_de_juros

# Exibindo o montante
print("O montante é: R$", montante)
'''
'''
# Exercício 3

# Solicitando os números iniciais
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Declarando os pesos das grandezas
p1 = 2/10
p2 = 3/10
p3 = 5/10

# Calculando a média ponderada
media_ponderada = (n1*p1 + n2*p2 + n3*p3)/(p1+p2+p3)

# Exibindo o resultado
print(media_ponderada)
'''
'''
#Exercício 4

# Solicitando o valor inicial de num
num = int(input("Digite um número inteiro: "))

# Incrementando num em uma unidade
num += 1

# Exibindo o resultado
print(num)
'''

'''
# Operadores relacionais

x = 1
print(x == 1)
print(x != 1)
print(x > 1)
print(x >= 1)
print(x < 1)
print(x <= 1)
'''
'''
# Exercício 5

# Solicitando um valor
x = float(input("Digite um número: "))

# Verificando se ele é positivo
positivo = x > 0

# Exibindo o resultado
print("O valor é positivo? ", positivo)
'''
'''
# Exercício 6

num = int(input("Digite um número: "))

resto = num % 5

print("O número é múltiplo de 5?", resto == 0)
'''