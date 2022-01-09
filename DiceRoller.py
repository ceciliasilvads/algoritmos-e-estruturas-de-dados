import random

def JogarDado():
    dice_size = int(input("Quantos lados tem seu dado? "))
    dice_rolls = int(input("Quantas vezes que quer joga o dado? "))
    player_name = str(input("Qual seu nome? "))
    dice_sum = 0

    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f"Número: {roll}! :(")
        elif roll == dice_size:
            print(f"Número: {roll}! :)")
        else:
            print(f"Número: {roll}! :|")

    print(f"Sua pontuação foi {dice_sum}, {player_name}!")

if __name__== "__main__":
    JogarDado()