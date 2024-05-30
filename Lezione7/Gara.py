
import random


print("BANG !!!!! AND THEY'RE OFF !!!!!")


def mossa_tartaruga(posizione):

    mossa = random.randint(1,10)


    if mossa >= 1 and mossa <= 5: # passo veloce
        posizione += 3
    elif mossa >= 6 and mossa <= 7: # scivolata
        posizione -= 6
    elif mossa >= 8 and mossa <= 10: # passo lento
        posizione += 1
    if posizione < 0:
        posizione = 0

    return posizione


def mossa_lepre(posizione):

    mossa = random.randint(1,10)


    if mossa >= 6 and mossa <= 7: # riposo
        pass
    elif mossa >= 6 and mossa <= 7: # grande balzo
        posizione += 9
    elif mossa == 5: # grande scivolata
        posizione -= 12
    if posizione < 0:
        posizione = 0
    elif mossa >= 8 and mossa <= 10: # piccolo balzo
        posizione += 1
    elif mossa >= 6 and mossa <= 7: # piccola scivolata
        posizione -= 2
    if posizione < 0:
        posizione = 0

    return posizione

def stampa_track(posizioni_gara):
    print("".join(posizioni_gara))



tartaruga = 0 # posizione iniziale
lepre = 0 # posizione iniziale

while True:


    tartaruga = mossa_tartaruga(tartaruga)
    lepre = mossa_lepre(lepre)

   
    posizioni_gara: list = ['_'] * 70


    if tartaruga == lepre:
        posizioni_gara[tartaruga] = 'OUCH'
    else:
        if tartaruga < len(posizioni_gara):
            posizioni_gara[tartaruga] = 'T'
        if lepre < len(posizioni_gara):
            posizioni_gara[lepre] = 'H'

    stampa_track(posizioni_gara)
    print(posizioni_gara)

    if tartaruga >= 69 and lepre >= 69:
        print("Tartaruga and lepre:")
        print("IT'S A TIE.")
        break

    elif tartaruga >= 69:
        print("TORTOISE WINS! || VAY!!!")
        break

    elif lepre >= 69:
        print("HARE WINS || YUCH!!!")
        break
    


