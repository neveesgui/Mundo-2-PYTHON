print("==== CALCULADORA DE MEDIA DE 2 NOTAS COM SITUAÇÃO ACADEMICA ====")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota : "))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f"Média do aluno: {media:.2f} | APROVADO! ")
elif media >= 5.0 and media <= 6.9:
    print(f"Média do aluno: {media:.2f} | RECUPERAÇÃO! ")
else:
    print(f"Média do aluno: {media:.2f} | REPROVADO! ")
