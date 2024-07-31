
class Calc:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def get_sum(self):

        return self.a + self.b


# RIPASSO PER ESAME

"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e 
l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e 
gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

"""

def rotate_left(elements: list, k: int) -> list:
    pass



# ESERCIZIO GESTIONE PRENOTAZIONE AEREE



from abc import ABC, abstractmethod

class Volo:

    def __init__(self, codice_volo: str, posti_disp: int):
        self.codice_volo: str = codice_volo
        self.posti_disp: int = posti_disp
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass


class VoloCommerciale(Volo):

    def __init__(self, codice_volo: str, posti_disp: int):
        super().__init__(codice_volo, posti_disp)
        self.posti_economica = posti_disp * 70 // 100
        self.posti_business = posti_disp * 20 // 100
        self.posti_prima = posti_disp * 10 // 100
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0


    def posti_disponibili(self)-> dict:

        available_seats = {}

        disponibili = self.posti_disp - self.prenotazioni
        if disponibili <= 0:
            disponibili = 0

        self.posti_economica -= self.prenotazioni_economica
        if self.posti_economica <= 0:
            self.posti_economica = 0

        self.posti_business -= self.prenotazioni_business
        if self.posti_business <= 0:
            self.posti_business = 0

        self.posti_prima -= self.prenotazioni_prima
        if self.posti_prima <= 0:
            self.posti_prima = 0

        available_seats = {'posti disponibili': disponibili, 'classe economica': self.posti_economica, 'classe business': self.posti_economica, 'prima classe':self.posti_prima}

        return available_seats



    def prenota_posto(self, posti: int, classe_servizio: str):
        self.posti: int = posti
        self.classe_servizio: str = classe_servizio
        
        if self.posti_disponibili()['posti disponibili'] > 0:
            if classe_servizio == self.posti_economica and self.posti_economica > 0:
                self.prenotazioni +=1
                print()



    
        


