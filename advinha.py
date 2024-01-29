import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = int(input("Digite um número: "))
        tentativas += 1

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número em", tentativas, "tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

jogo_adivinhacao()