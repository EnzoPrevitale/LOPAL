alfabeto = "abcdefghijklmnopqrstuvwxyz"
deslocamento = 3

with open("criptografado.txt", encoding="utf-8") as f:
    for linha in f:
        for char in linha:
            if char in alfabeto.upper():
                print(alfabeto.upper()[alfabeto.upper().index(char) - deslocamento], end="")
            elif char in alfabeto:
                print(alfabeto[alfabeto.index(char) - deslocamento], end="")
            else:
                print(char, end = "")
