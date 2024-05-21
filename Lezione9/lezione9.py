"""

def complex_statistical_function(x, distribution_type, **kwargs):

    if distribution_type == "geometric":

        p: float = kwargs["p"]


    elif distribution_type == "poisson":

        lambda_1: float = kwargs["lambda_1"]
"""

# Esercizi lezione 9

"""

Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
in genere utilizzando tutte le lettere originali esattamente una volta.

"""

def anagram(s: str, t: str) -> bool:
    if len(s) == len(t) and sorted(s.lower()) == sorted(t.lower()):
        return True
    else:
        return False
    
s = 'silent'
t = 'listen'
print(anagram(s, t))


"""
Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.

"""

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    queue: list[ListNode] = [head]
    
    while queue:
        curr_node = queue.pop()
        if curr_node:
            reversed_list.append(curr_node.val)
            queue.append(curr_node.next)
    return reversed_list[::-1]


# Funzione ricorsiva


def reverse_recursive(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    _reverse(head, reversed_list)
    return reversed_list[::-1]

def _reverse(curr_node: ListNode, reversed_list: list[int]):
    if curr_node:
        reversed_list.append(curr_node.val)
        _reverse(curr_node.next, reversed_list)
        

head = ListNode(val=0, 
                next=ListNode(val=1, 
                              next=ListNode(val=5, 
                                            next=ListNode(val=6))))
print(reverse(head))
    


"""

Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0 e restituire l'account.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

"""
    
class Account:
    
    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance
        
        
    def deposit(self, amount: float):
        self.balance = 0.0
        if amount > 0.0 and self.balance >= 0.0:
            self.balance += amount
        else:
            raise ValueError ("No money")
        

    def get_balance(self):

        return self.balance
        


class Bank:
    
    def __init__(self, account: dict[str, Account]):
        self.account: dict[str, Account] = account
        account = {}

    
    def create_account(self, account_id):
        if account_id in self.account.keys():
          raise ValueError("This account already exist")
        else:
            account = Account(account_id)
            self.account[Account] = account

        

    def deposit(self, account_id, amount):
        for x in self.account.keys():
            if x == account_id:
                self.account[x].balance += amount



    def get_balance(self, account_id):
        if account_id in self.account.keys():
            for x in self.account.keys():
                if x == account_id:
                    return self.account[x].balance
                
        else:
            raise ValueError("Not ID found")


'''

Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

    Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
    Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
    Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

Nota:

    Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
    Solo le celle riempite devono essere convalidate secondo le regole menzionate.

''' 

def sudoku(tavola: list[list[int]]) -> bool:
    rows: dict[int, list[int]] = {i: [] for i in range(9)}
    # rows = {0: [], 1: [], ... , 8: []}
    cols: dict[int, list[int]] = {i: [] for i in range(9)}
    squares: dict[int, list[int]] = {f'{i}-{j}': [] for i in range(3) for j in range(3)}
    # squares = dict[int, list[int]] = {i: [] for i in range(9)
    for i in range(9):
       for j in range(9):
           curr_elem: str = tavola[i][j]
           if curr_elem != '.':
                square_i, square_j = i // 3, j // 3
                # square_index = 3 * square_i + square_j
                # if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[square_index]
                if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[f'{square_i}-{square_j}']:
                    return False
                
                rows[i].append(curr_elem)
                cols[j].append(curr_elem)
                squares[f'{square_i}-{square_j}'].append(curr_elem)
                # squares[square_index].append(curr_elem)
    return True
                
# square_i = 0, square_j = 0 -> 0
# square_i = 0, square_j = 1 -> 1
# square_i = 0, square_j = 2 -> 2
# square_i = 1, square_j = 0 -> 3
# square_i = 1, square_j = 1 -> 4
# square_i = 1, square_j = 2 -> 5
# square_i = 2, square_j = 0 -> 6
# square_i = 2, square_j = 1 -> 7
# square_i = 2, square_j = 2 -> 8 ---> 3 * square_i + square_j
               