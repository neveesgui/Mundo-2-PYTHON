print("==== CONFEDERAÇÃO BRASILEIRA DE NATAÇÃO ====")
ano_nascimento = int(input("Em que ano você nasceu: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")
if idade <= 9:
    print("CATEGORIA MIRIM")
elif idade > 9 and idade <= 14:
    print("CATEGORIA INFANTIL")
elif idade > 14 and idade <= 19:
    print("CATEGORIA JUNIOR")
elif idade > 19 and idade <= 20:
    print("CATEGORIA SENIOR")
else:
    print("CATEGORIA MASTER")
