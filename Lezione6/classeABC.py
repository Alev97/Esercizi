

# CLASSE ASTRATTA


from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):

        pass

    
    @abstractmethod
    def movimento(self):

        pass


class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome = nome
        self.velocità = 10.0 # m/s

    def verso(self):
        print("Bau!")
    
    def movimento(self, t: int):
        print(self.velocità * t)
        

cane1: Cane = Cane(nome="Pluto")
cane1.verso()
cane1.movimento(t=10)

class Gatto(AbcAnimal):

    def __init__(self, nome:str) -> None:
        super().__init__()

        self.nome = nome
        self.velocità = 10.0 # m/s

    def verso(self):
        print("Miao!")

    def movimento(self, t:int):
        print(self.velocità * t)
        
    
gatto1: Gatto = Gatto(nome="Pippo")
gatto1.verso()
gatto1.movimento(t=10)



from typing import Any



class ContoBancario:

    total_accounts = 0
    definizione: str = 'ClasseContoBancario'

    def __init__(self, iban, saldo, nome):
        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        ContoBancario.total_accounts += 1

    def deposito(self, importo):
        
        self.saldo += importo
        print(f'{importo} depositato. Il nuovo saldo è {self.saldo}')

    def prelievo(self, importo):
        self.saldo += importo
        print(f'{importo} deposito. Il nuovo saldo è {self.saldo}')

    @classmethod
    def get_total_accounts(cls):
        print(f'Account totali creati: {cls.total_accounts}')

    @classmethod
    def get_type(cls):
        print(f'Type: {cls.definizione}')

    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print('Iban valido')
            return True
        else:
            print('Iban non valido')
            return False

account1 = ContoBancario(1234567890, 0, 'Alice')
account2 = ContoBancario(9876543210, 1000, 'Bob')

account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.prelievo(150)

ContoBancario.get_total_accounts()
ContoBancario.get_type()
account3 = ContoBancario(1234567890, 0, 'Bob')

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account('12345ABCD')

def valida_accounts(iban):
    if isinstance(iban, int) and len(str(iban)) == 10:
        print('iban valido')
        return True
    else:
        print('iban non valido')
        return False



class Filiale:

    filiali_create: int = 0

    def __init__(self, codice:str, indirizzo: str) -> None:
        self.codice = codice
        self.indirizzo = indirizzo

        Filiale.filiali_create += 1

    @classmethod
    def totale_filiali_create(cls) -> int:

        return cls.filiali_create



class Banca:

    def __init__(self, nome: str, simbolo: str) -> None:
        self.nome = nome
        self.simbolo = simbolo
        self.lista_filiali: list[Filiale] = []

    def numero_filiali(self):

        return len(self.lista_filiali)
    
    def aggiungi_filiale(self, filiale: Filiale):

        if self.simbolo in filiale.codice:
            self.lista_filiali.append(filiale)
        else:
            raise ValueError("La filiale appartiene ad un'altra banca")
    


unicredit: Banca = Banca(nome='Unicredit', simbolo='UCG')
intesa: Banca = Banca(nome='Intesa', simbolo='ISP')
filiale_unicredit_1: Filiale = Filiale(codice='UCG01', indirizzo='Via Sierra Nevada,60,Roma,Italia')
filiale_intesa1: Filiale = Filiale(codice='ISP01', indirizzo='Piazza Barberini,60,Roma,Italia')

unicredit.lista_filiali.append(filiale_unicredit_1)
intesa.lista_filiali.append(filiale_intesa1)

intesa.aggiungi_filiale(filiale_intesa1)
unicredit.aggiungi_filiale(filiale_unicredit_1)

print(unicredit.numero_filiali())
print(intesa.numero_filiali())
print(Filiale.totale_filiali_create())







