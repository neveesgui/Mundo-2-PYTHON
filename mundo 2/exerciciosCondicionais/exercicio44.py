print("==== DESCONTOS PARA PRODUTO ====")
valor_produto = float(input("Qual o valor do produto R$: "))
print(
    "[1] à vista: Cinheiro ou Cheque\n[2] à vista: Cartão\n[3] Cartão: Parcelado em 2x\n[4] Cartão: Parcelado em 3x"
)
pagamento = input("Selecione a forma de pagamento: ")

if pagamento == "1":
    desconto = valor_produto * 0.10
    valor_total = valor_produto - desconto
    print(f"Voce ganhou R${desconto} de desconto! Referente a 10% pelo metodo de pagamento.")
    print(f"O Valor total: R${valor_total:.2f}")
elif pagamento == "2":
    desconto = valor_produto * 0.05
    valor_total = valor_produto - desconto
    print(f"Voce ganhou R${desconto:.2f} de desconto! Referenet a 5% pelo metodo de pagamento.")
    print(f"Valor total: R${valor_total:.2f}")
elif pagamento == "3":
    valor_total = valor_produto
    print("Não possui desconto ativo!")
    print(f"Valor total: R${valor_total:.2f}")
elif pagamento == "4":
    acrescimo = valor_produto * 0.20
    valor_total = valor_produto + acrescimo
    print(
        f"Acrescimo de R${acrescimo:.2f} no valor da sua compra! Referente ao metodo de pagamento."
    )
    print(f"Valor total: R${valor_total:.2f}")
