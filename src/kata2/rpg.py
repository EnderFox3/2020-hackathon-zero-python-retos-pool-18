#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    password = [0]

    for value in range(0,passLen):
        numeros = random.randint(0,10)
        letras = random.choice(string.ascii_letters)
        simbolos = chr(random.randint(33,59))
        aleatorio=random.randint(1,4)
        #print(simbolos)
        if aleatorio==1:
            password.append(numeros)
            
        if aleatorio == 2:
            password.append(letras)
            
        if aleatorio == 3:
            password.append(simbolos)    
    #
    #

    return print(password)
RandomPasswordGenerator()