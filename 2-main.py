# Exercício 01
'''
nome = "Enzo"
idade = 16

# Exibindo os valores das variáveis
print(f"Olá, meu nome é {nome}, e tenho {idade} anos.")
'''
###
'''
# Exercício 02

# Declarando as variáveis
nome1 = 'aula'
nome2 = 'Python'

# Exibindo os valores iniciais das variáveis
print(nome1, nome2)

# Alterando os valores das variáveis
nome3 = nome1

nome1 = nome2
nome2 = nome3

# OU

nome1, nome2 = nome2, nome1

# Exibindo os valores alterados das variáveis
print(nome1, nome2)
'''
###
'''
# Exercício 03

# Declarando as variáveis
nome = 'Enzo'
sobrenome = 'Previtale'

# Concatenando as variáveis
nome_sobrenome = nome + ' ' + sobrenome

# Exibindo as variáveis
print(nome_sobrenome)
'''
'''
# Exercício 04

# Declarando a primeira variável
numero = 8

# Declarando a segunda variável, convertendo a primeira para o tipo float com a função float()
numero2 = float(numero)

# Exibindo a variável
print(numero2)
'''
###
'''
# Exercício 05

# Declarando a array alimento
alimento = ['pão com manteiga', "pão com presunto", "bolo"]

# Declarando a string com os alimentos
frase = f"Hoje, eu vou pegar um {alimento[0]}, um {alimento[1]} e um {alimento[2]} no café da manhã."

# Exibindo a frase
print(frase)
'''
###

# Exercício 06
'''
# Declarando as variáveis
dia = 11
mes = 2
ano = 2025

# Concatenando as variáveis em uma nova string
data = "%02d" % dia + "/" + "%02d" % mes + "/" + "%02d" % ano

# Exibindo as variáveis
print(data)
'''
# Exercício 07

# Declarando a variável
frase = 'Python'

# Declarando a variável com parte da primeira string
frase2 = frase[:3]

# Exibindo a variável
print(frase2)