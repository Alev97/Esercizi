
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