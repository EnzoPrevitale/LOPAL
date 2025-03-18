# 08

# Solicitando a idade e renda mensal do cliente
idade = int(input("Digite a sua idade: "))
renda_mensal = float(input("Digite a sua renda mensal: "))

# Verificando a elegibilidade do cliente
elegivel = False # Cliente inelegível
if idade >= 18: # Cliente maior de idade
    if renda_mensal > 1500: # Renda mensal acima de R$1500,00
        elegivel = True # Cliente elegível
else: # Cliente menor de idade
    if renda_mensal > 1000: # Renda mensal acima de R$1000,00
        elegivel = True # Cliente elegível

# Analisando e imprimindo o resultado
if elegivel:
    print("Você é elegível para fazer empréstimos.")
else:
    print("Você não é elegível para fazer empréstimos.")