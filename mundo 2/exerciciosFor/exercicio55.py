maior = None
menor = None
for i in range(1, 5):
    peso = float(input(f"Informe o peso da {i}ª pessoa em kg: "))

    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso
print(f"O maior peso foi: {maior}kg")
print(f"O menor peso foi: {menor}kg")
