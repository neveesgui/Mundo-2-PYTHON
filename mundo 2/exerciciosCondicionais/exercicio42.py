print("==== DESCUBRA O TIPO DO TRIANGULO ====")
lado_a = float(input("Digite o valor: "))
lado_b = float(input("Digite outro valor: "))
lado_c = float(input("Digite o ultimo valor: "))
if lado_a == lado_b == lado_c:
    print("equilatero")
elif lado_a != lado_b != lado_c != lado_a:
    print("escaleno")
else:
    print("isoceles")
