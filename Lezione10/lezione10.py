
'''
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51

'''

def print_seq(): 
    
    print("Sequenza a):")
    a = [1, 2, 3, 4, 5, 6, 7]
    for i in range(1,8):
        print(i)
    print()

    print("Sequenza b):")
    b = [3, 8, 13, 18, 23]
    for i in range(3,24,5):
        print(i)
    print()

    print("Sequenza c):")
    c = [20, 14, 8, 2, -4, -10]
    for i in range(20,-11,-6):
        print(i)
    print()

    print("Sequenza d):")
    d = [19, 27, 35, 43, 51]
    for i in range(19,52,8):
        print(i)
    print()


'''
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    new_dict = {}

    for key,value in dict1.items():
        new_dict[key] = value

    for key,value in dict2.items():
        new_dict[key] = value

        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value

    return new_dict
    
