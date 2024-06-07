
class Prodotto:

    def __init__(self, nome: str, quantità: int):
        self.nome: str = nome
        self.quantità: int = quantità

class Magazzino:

    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.prodotto: Prodotto = prodotto

        if prodotto.nome == prodotto.nome:
            for prodotto in self.prodotti:
                prodotto.quantità += prodotto.quantità
            return
        self.prodotti.append(prodotto)


    def crea_prodotto(self, nome: str) -> Prodotto:
        self.nome: str = nome

        for prodotto in self.prodotti:
            if nome == prodotto.nome:
                return prodotto
            else:
                print(f"Il prodotto {nome} è esaurito.")


    def verifica_disponibilità(self, nome: str) -> str:
        self.nome: str = nome

        for prodotto in self.prodotti:
            if nome == prodotto.nome:
                print(f"{prodotto.quantità} {nome}.")
            else:
                print ('Prodotto non disponibile.')

maga1: Magazzino = Magazzino()
prodotto1: Prodotto = Prodotto('Penne', 500)
maga1.aggiungi_prodotto(prodotto1)

print(maga1.crea_prodotto('Penne'))
print(maga1.verifica_disponibilità('Penne'))

print(maga1.verifica_disponibilità('Gomme'))