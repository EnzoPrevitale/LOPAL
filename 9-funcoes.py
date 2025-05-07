'''
def area(largura, comprimento):
    return largura * comprimento

print(f"O valor da área é {area(float(input("Digite a largura, em m: ")),float(input("Digite o comprimento, em m: ")))} m².")
'''
'''
def alterar_valor():
    global z
    z = 10

z = 5
alterar_valor()
print(z)
'''
'''
def ler():
    print(texto)

texto = "Hello World!"

ler()
'''

'''
def f():
    print("aaaaaaa")


magu = f()

print(magu)
'''

# 01
'''
def dobro(num):
    return 2 * num

numero = float(input("Digite um número para calcular o dobro: "))
print(dobro(numero))
'''
# 02
""""
def maior(num1, num2):
    numeros = [num1, num2]
    return max(numeros)


print(f"O maior dos números digitados é {maior(float(input("Digite um número: ")), float(input("Digite outro número: ")))}")
"""
# 03
'''
def media(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma / len(lista)

print(media([45,99]))
'''
# 04

def calcular_fatorial(numero):
    produto = 1
    for i in range(1, numero + 1):
        produto *= i

    return produto

num = int(input("Digite um número: "))
print(calcular_fatorial(num))