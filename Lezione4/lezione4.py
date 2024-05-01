
# GLI ESERCIZI VERI INIZIANO DALLA LINEA 65

'''
# Esercizio 1

def subtract (x: float, y: float):
    subtract = x - y
    return subtract

x = 15
y = 7
out = subtract(x, y)
print(out)

# Esercizio 2

def check_value(x: int):
    if x > 5:
        print(f'{x} è maggiore di 5')
    elif x < 5:
        print(f'{x} è minore di 5')
    else:
        print(f'{x} è uguale a 5')

check_value(22)

# Esercizio 3

def check_lenght(x: str):
    if len(x) > 10:
        print(f'{x} è più lunga di 10 caratteri')
    elif len(x) < 10:
        print(f'{x} è più corta di 10 caratteri')
    else:
        print(f'{x} è uguale a 10 caratteri')

check_lenght('mammamia')

# Esercizio 4

def print_numbers(x: list):
    for i in x:
        print(i)

lista: list = [3, 4, 5, 6]
print_numbers(lista)

# Esercizio 5

def check_each(x: list):
    for i in x:
        if i > 5:
            print(f'{i} è maggiore di 5')
        elif i < 5:
            print(f'{i} è minore di 5')
        else:
            print(f'{i} è uguale a 5')
     
x: list = [7, 5, 3]
check_each(x)
'''
#############################################

'''
8-1. Message: Write a function called display_message() 
that prints one sentence telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
'''
def display_massage():
    print('In this chapter I am learning how to solve a problem and how to use functions in Python')
display_massage()

'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
'''

def favorite_book(title):
    print(f'One of my favorite books is {title}')
favorite_book('Supersantos')
