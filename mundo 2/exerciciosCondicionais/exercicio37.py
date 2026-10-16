print("==== CONVERSOR DE NUMERO INTEIRO PARA BINARIO | OCTAL | HEXADECIMAL ====")
numero = int(input("Digite um número inteiro: "))
conversao = int(input("Escolha uma opção para converter [1]binario [2]octal [3]hexdeciaml: "))
binario = bin(numero)
octal = oct(numero)
hexadecimail = hex(numero)
if conversao == 1:
    print(f"O número {numero} convertido para binario é: {binario}")
elif conversao == 2:
    print(f"O número {numero} convertido para octal é: {octal}")
elif conversao == 3:
    print(f"O número {numero} convertido para hexadecimal é: {hexadecimail}")
else:
    print("ERRO!")
