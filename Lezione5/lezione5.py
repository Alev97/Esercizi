
'''
ESERCIZIO 3 RIPASSO LEZIONE 5

Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
'''

def check_access(username: str, password: int, is_active: bool) -> str:
   if username == 'admin' and password == '12345' and is_active:
      return 'Accesso consentito'
   else:
      return 'Accesso negato'

result = check_access('admin','37438',True)
print(result)

'''
ESERCIZIO 1 RIPASSO LEZIONE 5

La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.

Trova l'errore e correggi il codice affinché soddisfi i casi di test.

'''

# CODICE CORRETTO

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers) 
    
'''

ESERCIZIO 5 RIPASSO LEZIONE 5

La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati.
 
TROVA L'ERRORE E CORREGGI IL CODICE

'''

# CODICE CORRETTO

def find_element(lst: list[int], element: bool) -> bool:
    for item in lst:
        if item == element:
            return True
        return False
    
'''
ESERCIZIO 2 PIASSO LEZIONE 5

Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

'''

mylist = [1,4,5,3,6,3,8,'ciao','pino','mago','freddo','ciao','pino',3,7,]

def remove_duplicates(mylist) -> list:
    newlist = [] 
    for i in mylist: 
        if i not in newlist: 
            newlist.append(i) 
    return newlist 

'''
ESERCIZIO 7 RIPASSO LEZIONE 5

Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

'''
 
  
def check_parentheses(expression: str) -> bool:
    aperte = 0
    chiuse = 0

    for i in expression:
        if i == '(':
            aperte += 1
        else:
            chiuse += 1
            if chiuse > aperte:
                return False
    if aperte == chiuse and expression[0] == '(':
        return True
    else: 
        return False







