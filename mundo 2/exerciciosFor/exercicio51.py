primeiro_termo = int(input("Digite o valor do primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
pa = primeiro_termo + (10 - 1) * razao
termos = list(range(primeiro_termo, pa + razao, razao))
print(f"O resultado da Progressão Artitmetica: {pa}")
print(termos)
