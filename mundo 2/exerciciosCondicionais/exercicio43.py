print("==== CALCULO IMC ====")
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite seu peso em metros: "))
imc = peso / (altura**2)
print(f"Seu IMC: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc <= 25:
    print("Você está no peso ideal!")
elif imc >= 25 and imc <= 30:
    print("Você está com Sobrepeso")
elif imc >= 30 and imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida!")
