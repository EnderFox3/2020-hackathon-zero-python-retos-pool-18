from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == ai:
        return "Empate!"
    elif player.lower()== options[0].lower() and player.lower() == options[2]:
        return "Ganaste!"
    elif player.lower()== options[1].lower() and player.lower() == options[0]:
        return "Ganaste!"
    elif player.lower()== options[2].lower() and player.lower() == options[1]:
        return "Ganaste!"
    else:
        return "Perdíste!"

# Entry Point
def Game():
    #
    #
    aleatorio= randint(0,3)
    ai=options[aleatorio]
    #
    #

    #
    #
    
    winner = quienGana(player, ai)

    print(winner)


player=input("Seleciona entre: Piedra, Papel o Tijera: ")

Game()