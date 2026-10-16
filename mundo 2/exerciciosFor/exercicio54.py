ano_atual = 2026
maior = 0
menor = 0
for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano que a {i}ª nasceu: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"Tivemos {maior} pessoa maiores de idade.")
print(f"Tambem tivemos {menor} pessoas menores de idade.")
