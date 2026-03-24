import random

numero_secreto = random.randint(1, 20)

print("Jogo de adivinhação")
print("Você tem 5 tentativas")

for tentativa in range(5):
    numero_escolhido = int(input("Por favor, escolha um número entre 1 e 20: "))

    if numero_escolhido == numero_secreto:
        print("Parabéns, você acertou")
        break
    elif numero_escolhido < numero_secreto:
        print("Muito baixo")
    else:
        print("Muito alto")
else:
    print("Fim de jogo")

print(f"O número secreto foi: {numero_secreto}")