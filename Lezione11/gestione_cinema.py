
# Sistema di Prenotazione Cinema


class Film:

    def __init__(self, titolo: str, durata: float):
        self.titolo: str = titolo
        self.durata: float = durata





class Sala:
 
    def __init__(self, num_ident: int, film: str, posti_tot: int, posti_prenotati: int):
        self.num_ident: int = num_ident
        self.film: str = film
        self.posti_tot: int = posti_tot
        self.posti_prenotati: int = posti_prenotati
        self.sala = None




    def prenota_posti(self, num_posti: int):
        self.num_posti: int = num_posti

        if self.num_posti < self.posti_tot:
            self.posti_prenotati += 1
            return 'Confermato'
        else:
            return 'Errore'
          


    def posti_disponibili(self):

        return self.posti_tot - self.posti_prenotati





class Cinema:


    def __init__(self, sala: Sala):

        self.sala: list[Sala] = []



    def aggiungi_sala(self, sala: Sala):
        self.sala: Sala = sala



    def prenota_film(self, titolo_film: str, num_posti: int):
        self.titolo_film: str = titolo_film
        self.num_posti: int = num_posti








