
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

'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text 
of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
'''

def make_shirt(size,message):
    print(f"The size is {size} and the message is: {message}.")
make_shirt('M',"Don't worry, be happy")
make_shirt(size = 'XXL', message = 'Carpe diem')

'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message 
that reads I love Python. Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message.
'''

def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the message to be printed is: '{message}'.")
make_shirt('L','I love Python')
make_shirt(size = 'M', message = 'I love Python')
make_shirt(size = 'XS', message = 'I love Carbonara')

'''
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
'''

def describe_city(city, country):
    print(f'{city} is in {country}')
describe_city('Madrid','Spain')
describe_city('Sevilla','Spain')
describe_city('Oslo','Norway')






