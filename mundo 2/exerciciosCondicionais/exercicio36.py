print("==== CALCULO COMPRA DE CASA ====")
valor_casa = float(input("Digite o valor da casa em R$: "))
salario = float(input("Digite o seu salario R$: "))
anos = int(input("Em quantos anos voce quer pagar: "))
parcela_mensal = valor_casa / (anos * 12)
if parcela_mensal > (salario * 0.3):
    print(
        f"Emprestimo Negado! A parcela mensal de R${parcela_mensal:.2f} excede 30% do seu salario."
    )
else:
    print(f"Emprestimo Aprovado! A parcela mensal será de R${parcela_mensal:.2f}.")
