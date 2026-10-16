mulheres = 0
soma_idade = 0
homem_velho = ""
homem_maior_idade = 0
for i in range(4):
    nome = input("Informe o seu nome: ")
    idade = int(input("informe a sua idade: "))
    sexo = input("Informe o seu sexo: ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    soma_idade += idade
    if sexo == "feminino" and idade < 20 and idade >= 0:
        mulheres += 1
    if sexo == "masculino" and idade > homem_maior_idade:
        homem_maior_idade = idade
        homem_velho = nome
media_idades = soma_idade / 4

print(f"A media das idades é: {media_idades}")
print(f"mulheres com menos de 20 anos: {mulheres}")
print(f"homem mais velho: {homem_velho}")
