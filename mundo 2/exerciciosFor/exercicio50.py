soma = 0
for i in range(7):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        soma += numero
print(f"A soma dos numeros pares é: {soma}")
