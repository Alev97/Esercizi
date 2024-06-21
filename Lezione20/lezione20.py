
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


####


# GESTIONALE PAGAMENTO


class Pagamento:

    def __init__(self):
        self._importo = None


    def get(self):

        return self._importo


    def set(self, importo: float):
        self._importo = importo

    
    def dettagliPagamento(self):

        print(f"Importo del pagamento: {self._importo}")


class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__(self._importo)


    def dettagliPagamento(self):

        print(f"{self._importo} da pagare in contanti:")


    def inPezziDa(self):

        soldi: list[float] = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]

        






class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome_titolare_carta: str, data_scadenza: str, numero_carta: int):
        super().__init__(self._importo)
        self.nome_titolare_carta: str = nome_titolare_carta
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta


