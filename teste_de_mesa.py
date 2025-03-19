# Condicionais

# 01
'''
# Solicitando um ano ao usuário
ano = int(input("Digite um ano: "))

# Verificando se o ano é bissexto
if ano % 4 == 0:
    bissexto = True
else:
    bissexto = False

# Imprimindo o resultado
if bissexto:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
'''
# 02
'''
# Solicitando o peso e a altura do usuário
peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite a sua altura, em m: "))

# Calculando o IMC do usuário
imc = peso/altura**2

# Definindo a classificação do IMC do usuário
if imc < 18.5:
    classificacao = "Baixo peso"
elif imc < 25:
    classificacao = "Normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade mórbida"

# Imprimindo o IMC e a classificação do usuário
print(f"O seu IMC é {imc}kg/m². A sua classificação é {classificacao}.")
'''
# 03
'''
# Solicitando a quuantidade de produtos e o valor unitário ao usuário
quantidade_produtos = int(input("Digite a quantidade de produtos a ser adquirida: "))
valor_unitario = float(input("Digite o valor unitário do produto: "))

# Calculando o desconto para cada quantidade
if quantidade_produtos > 100:
    desconto = 10/100
else:
    desconto = 5/100

# Calculando o valor inicial, o valor final e o valor descontado
valor_inicial = quantidade_produtos * valor_unitario
valor_final = valor_inicial - desconto*valor_inicial
valor_descontado = valor_inicial - valor_final

# Exibindo o valor inicial, o valor final e o valor descontado
print(f" Valor Unitário: R${valor_unitario} \n Quantidade: {quantidade_produtos} \n Valor inicial: R${valor_inicial} \n Desconto obtido: {desconto*100}% \n Valor descontado: R${valor_descontado} \n Valor final: R${valor_final}")
'''
# 04
'''
# Solicitando a idade do usuário
idade = int(input("Digite a sua idade: "))

# Definindo o tipo de voto
if idade < 16:
    # Não votante
    voto = "Não eleitor"
elif idade < 18:
    # Facultativo
    voto = "Facultativo"
else:
    # Obrigatório
    voto = "Obrigatório"

# Exibindo o resultado
if voto != "Não eleitor":
    print(f"O seu voto é {voto.lower()}.")
else:
    print(f"Você não é elegível para votar.")
'''
# 05
'''
# Solicitando as idades das três pessoas
idade = [int(input("Digite a idade da primeira pessoa: ")), int(input("Digite a idade da segunda pessoa: ")), int(input("Digite a idade da terceira pessoa: "))]

# Verificando qual idade é a maior
if idade[0] > idade[1] and idade[0] > idade [2]:
    # idade[0] é maior
    maior_idade = idade[0]

    # Verificando a menor idade
    if idade[1] > idade[2]:
        # idade[2] é menor
        menor_idade = idade[2]
    elif idade[1] < idade[2]:
        # idade[1] é menor
        menor_idade = idade[1]
    else:
        # idade[1] e idade[2] são as menores
        menor_idade = idade[1]

elif idade[1] > idade[0] and idade[1] > idade[2]:
    # idade[1] é maior
    maior_idade = idade[1]

    # Verificando a menor idade
    if idade[0] > idade[2]:
        # idade[2] é menor
        menor_idade = idade[2]
    elif idade[0] < idade[2]:
        # idade[0] é menor
        menor_idade = idade[0]
    else:
        # idade[0] e idade[2] são menores
        menor_idade = idade[2]

elif idade[2] > idade[0] and idade[2] > idade[1]:
    # idade[2] é maior
    maior_idade = idade[2]

    # Verificando a menor idade
    if idade[0] > idade[1]:
        # idade[1] é menor
        menor_idade = idade[1]
    elif idade[0] < idade[1]:
        # idade[0] é menor
        menor_idade = idade[0]
    else:
        # idade[0] e idade[1] são menores
        menor_idade = idade[1]

elif idade[0] == idade[1] and idade[0] > idade[2]:
    # idade[0] é maior e idade[2] é menor
    maior_idade = idade[0]
    menor_idade = idade[2]
elif idade[0] == idade[2] and idade[0] > idade[1]:
    # idade[0] é maior e idade[1] é menor
    maior_idade = idade[0]
    menor_idade = idade[1]
else:
    # idade[1] é maior e idade [0] é menor
    maior_idade = idade[1]
    menor_idade = idade[0]

# Imprimindo os resultados
print(f"A maior idade é {maior_idade} e a menor idade é {menor_idade}.")
'''
# 06
'''
# Solicitando as horas, os minutos e os segundos
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

# Verificando se os números estão nos intervalos corretos
if hora >= 0 and hora < 24:
    # Hora válida
    print("A hora é valida.")

    if minuto >= 0 and minuto < 60:
        # Minuto válido
        print("O minuto é válido.")

        if segundo >= 0 and minuto < 60:
            # Segundo válido
            print("O segundo é válido.")

            # Imprimindo o horário
            print(f"{hora}:{minuto}:{segundo}")
        else:
            # Segundo inválido
            print("O segundo é inválido.")
    else:
        # Minuto inválido
        print("O minuto é inválido.")
else:
    # Hora inválida
    print("A hora é inválida.")
'''
# 07
'''
# Solicitando a nota
nota = float(input("Digite o valor numérico da nota: "))

# Convertendo para letra
if nota > 10:
    # Nota inválida
    print("Nota inválida.")
elif nota > 9:
    # A
    nota = 'A'
elif nota > 7:
    # B
    nota = 'B'
elif nota > 5:
    # C
    nota = 'C'
elif nota > 3:
    # D
    nota = 'D'
elif nota >= 0:
    # E
    nota = 'E'
else:
    # Nota inválida
    print("Nota inválida.")

# Imprimindo a nota em letra
print(f"A nota do aluno é {nota}.")
'''
# 08
'''
# Solicitando o valor dos lados
lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))
lado_d = float(input("Digite o valor do lado D: "))

# Verificando se os lados paralelos têm valores iguais
if lado_a == lado_c and lado_b == lado_d:
    # Retângulo
    print("Os valores digitados correspondem a um retângulo.")
    if lado_a == lado_d:
        # Quadrado
        print("Os valores digitados correspondem a um quadrado.")
else:
    # Não retângulo
    print("Os valores digitados não correspondem a um retângulo.")
'''