from random import choice

jogador = input("Escolha: ")
game = "Pedra", "Papel", "Tesoura"
sorteio = choice(game)
print("=======GAME=======")
print(f"Você: {jogador}\nMachine: {sorteio}")
print("=======GAME=======")
