
def ciao(name: str):

    return f'Ciao, {name}'

def salve(name: str):

    return f'Salve, {name}'

def saluta_bob(func):

    return func('Bob')

print(saluta_bob(ciao))
print(saluta_bob(salve))


#####


def parent():

    print('Sono in parent')

    def first_child():

        print('Sono in first_child')

    return first_child
    

print(parent())


####


def decorator(func):

    def wrapper():
        import time

        start = time.time()

        func()

        print(f"Time elapsed: {time.time() - start}")

    return wrapper


def ciao():

    print(f"Caio")

ciao = decorator(ciao)

ciao()