
# RIPASSO

'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

'''

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dict_nums = {'pari': [], 'dispari': []}

    for nums in classifica_numeri:
        if nums %2 == 0:
            dict_nums['pari'].append(nums)
        else:
            dict_nums['dispari'].append(nums)

    return dict_nums

lista = [1,2,3,4,5,6,7,8]

'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.

'''

def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    invert_dict = {}
    
    for key, value in dizionario.items():
        if value not in invert_dict:
            invert_dict[value] = key

    return invert_dict

'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    risultato = lista[:]
    
    for elemento, count in da_rimuovere.items():
        while count > 0 and elemento in risultato:
            risultato.remove(elemento)
            count -= 1
    
    return risultato

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))

        




'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

'''

def aggrega_voti(registro: list[dict]) -> dict:
    nuovo_registro = {}

    for studente in registro:
        nome = studente['name'] 
        voto = studente['voto']

        if nome in nuovo_registro:
            nuovo_registro[nome].append(voto)
            print(nuovo_registro[nome])
        else:
            nuovo_registro[nome] = [voto]

    return nuovo_registro

print(aggrega_voti([{'name': 'Alice', 'voto': 9}, {'name': 'Bob', 'voto': 7}, {'name': 'Alice', 'voto': 8}]))

'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario 
con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

'''









'''

PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare,
e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

'''

def create_contact(name: str, email: str = None, telefono: int = None) -> dict:
    contatto = {'profile':name, 'email': email, 'telefono': telefono}

    return contatto

contatto1 = create_contact('Mario Rossi','mario.rossi@gmail.com')
print(contatto1)

def update_contact(contatto: dict, name: str, email: str = None, telefono: int = None) -> dict:
    if contatto['profile'] == name:
        if email:
            contatto['email'] = email
        if telefono:
            contatto['telefono'] = telefono

    return contatto

contatto1 = update_contact(contatto1, 'Mario Rossi', telefono = 46846846848)
print(contatto1)

