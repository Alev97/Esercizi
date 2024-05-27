
import random


print("BANG !!!!! AND THEY'RE OFF !!!!!")

def posizioni_gara():
    mossa: list = ['_'] * 70

    if mossa_lepre == mossa_lepre:
        print("OUCH")

    


    






def mossa_tartaruga():
    
    mossa = random.randint(1,10)


    if mossa >= 1 and mossa <= 5: # passo veloce
        posizione += 3
    elif mossa >= 6 and mossa <= 7: # scivolata
        posizione -= 6
        if posizione <= 1:
            posizione = 1
    else: 
        mossa >= 8 and mossa <= 10: # passo lento
        posizione += 1


def mossa_lepre():
    
    mossa = random.randint(1,10)

    if mossa >= 6 and mossa <= 7: # riposo
        posizione = 0
    elif mossa >= 6 and mossa <= 7: # grande balzo
        posizione += 9
    elif mossa == 5: # grande scivolata
        posizione -= 12
        if posizione <= 1:
            posizione = 1
    elif mossa >= 8 and mossa <= 10: # piccolo balzo
        posizione += 1
    elif mossa >= 6 and mossa <= 7: # piccola scivolata
        posizione -= 2
        if posizione <= 1:
            posizione = 1

while True:

    tartaruga = 1 # posizione iniziale
    lepre = 1 # posizione iniziale

    tartaruga += mossa_tartaruga()
    lepre += mossa_lepre()

    if tartaruga <= 1:
        tartaruga = 1
    elif lepre <= 1:
        lepre = 1

    elif  tartaruga >= 70 and lepre >= 70:
        print("Tartaruga and lepre:")
        print("IT'S A TIE.")
    
    elif tartaruga >= 70:
        print("TORTOISE WINS! || VAY!!!")
    else:
        lepre >= 70:
        print("HARE WINS || YUCH!!!")

    


