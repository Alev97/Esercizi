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
               

'''

Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

    L'elemento in posizione 0 corrisponde alla radice
    Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
    Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
    Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.


'''

# METODO 1 SENZA CLASSE

# [1,2,3,4,5,6]
# elemento in pos. 0 (1) -> radice
# per elem in pos. i -> il figlio a sx si trova in pos. 2*i +1
# per elem in pos. 1 -> il figlio a dx si trova in pos. 2*(i+1) = 2*i + 2
#              1
#            /   \
#           2     2
#          / \   / \
#         4   5 4   5


def is_symmetric(tree: list[int]) -> bool:
    return are_mirrored(tree, 1, 2)

def are_mirrored(tree, left_index, right_index) -> bool:
    if left_index >= len(tree) and right_index >= len(tree):
        return True
    elif left_index >= len(tree) and right_index < len(tree) or (left_index < len(tree) and right_index >= len(tree)):
        return False
    if tree[left_index] != tree[right_index]:
        return False
    
    left_of_left = 2 * left_index + 1
    right_of_left = 2 * left_index + 2

    left_of_right = 2 * right_index + 1
    right_of_right = 2 * right_index + 2

    is_symmetric_external: bool = are_mirrored(tree, left_of_left, right_of_right)
    is_symmetric_internal: bool = are_mirrored(tree, right_of_left, left_of_right)

    return is_symmetric_internal and is_symmetric_external



# METODO 2 SENZA CLASSE (DI LUCA)


def is_symmetric_luca(tree: list[list]) -> bool:
    tree_dict: dict[str, list[int]] = {}
    tree_dict['0-a'] = [tree[1]]
    tree_dict['0-b'] = [tree[2]]

    for i in range(len(tree) // 2):
        if 2 * (i + 1) < len(tree):
            tree_dict[f'{i}-a'] = [tree[2*i+1], tree[2*(i+1)]]
            tree_dict[f'{i}-b'] = [tree[2*(i+1)+1], tree[2*((i+1)+1)]]
    
    for i in range(len(tree_dict) // 2):

        if tree_dict[f'{i}-a'] != list(reversed(tree_dict[f'{i}-b'])):
            return False
        
    return True


# METODO CON LA CLASSE


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=2))
        
def is_symmetric_with_class(root: TreeNode) -> bool:

    def are_mirrored(left: TreeNode, right:TreeNode) -> bool:
        if not left and not right:
            return True
        if not left and not right:
            return False
        
        if left.val != right.val:
            return False
        
        is_symmetric_external: bool = are_mirrored(left.left, right.right)
        is_symmetric_internal: bool = are_mirrored(right.left, left.right)

        return is_symmetric_internal and is_symmetric_external
    
    return are_mirrored(root.left, root.right)

def build_tree(tree: list[int]) -> TreeNode:
    # tree = [1,2,3,None,4,None,5]
    nodes = []
    for val in tree:
        if val:
            nodes.append(TreeNode(val))
        else:
            nodes.append(None)
    # figlio a sx sta in 2*i+1
    # figlio a dx sta in 2*i+2
    for i in range(len(nodes) // 2):
        if nodes[i]:
            left_index = 2*i + 1
            right_index = 2*i + 2
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]

    return nodes[0]

#def is_symmetric_vl:
    



'''

Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni.
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e 
l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e 
gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

'''

def rotate_left(elements: list, k: int) -> list:
    
    k = k % len[elements]

    while k > 0:
        first_elem = lista[0]  
        lista = lista[1:] + [first_elem]  
        k -= 1
    
    return lista

lista = [1,2,3,4,5,6,7,8,9]
k = 5
lista_ruotata_sx = rotate_left(lista, k)
print(lista_ruotata_sx)








   
    