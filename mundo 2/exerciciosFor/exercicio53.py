frase = input("Digite uma frase: ")
frase_limpa = frase.lower().replace(" ", "")
frase_invertida = ""

for i in range(len(frase_limpa) - 1, -1, -1):
    frase_invertida += frase_limpa[i]

print(f"A frase invertida é: {frase_invertida}")

if frase_limpa == frase_invertida:
    print("A frase é um Palindromo")
else:
    print("A frase NAO É um Palindromo")
