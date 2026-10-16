print("==== ALISTAMENTO MILITAR PELO ANO DE NASCIMENTO ====")
ano_nascimento = int(input("Em que ano você nasceu: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Voce nasceu no ano: {ano_nascimento} e tem idade: {idade} anos")

if idade == 18:
    print("voce esta apto para o alistamento militar")
elif idade > 18:
    saldo = idade - 18
    ano_alistamento = ano_atual - saldo
    print(f"Voce deveria ter se alistado há {saldo} anos atrás")
    print(f"O ano para seu alistamento foi em {ano_alistamento}")
else:
    saldo = 18 - idade
    ano_alistamento = ano_atual + saldo
    print(f"Voce ainda não esta apto, faltam {saldo} anos")
    print(f"O ano para seu alistamento será {ano_alistamento}")
