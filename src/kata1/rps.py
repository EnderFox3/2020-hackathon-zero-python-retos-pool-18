from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    return ""

# Entry Point
def Game():
    #
    #
    ai=options[randint(0,3)]

    #
    #
    
    winner = quienGana(player, ai)

    print(winner)


player=input("Seleciona entre: Piedra, Papel o Tijera: ")

Game()