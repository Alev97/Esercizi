
# Sistema di Prenotazione Cinema


class Film:

    def __init__(self, titolo: str, durata: float):
        self.titolo: str = titolo
        self.durata: float = durata



class Sala:

    def __init__(self, num_ident: int, posti_tot: int, posti_prenotati: int, film_adesso: Film = None):
        self.num_ident: int = num_ident
        self.film_adesso: Film = film_adesso
        self.posti_tot: int = posti_tot
        self.posti_prenotati: int = posti_prenotati
        self.sale = None



    def prenota_posti(self, num_posti: int):
        self.num_posti: int = num_posti

        if self.num_posti < self.posti_tot:
            self.posti_prenotati += num_posti
            return 'Confermato'
        else:
            return 'Errore'



def posti_disponibili(self):

    return self.posti_tot - self.posti_prenotati



class Cinema:


    def __init__(self, sale: list[Sala] = []):

        self.sale: list[Sala] = sale


    def aggiungi_sala(self, sala: Sala):

        self.sale.append(sala)



    def prenota_film(self, titolo_film: str, num_posti: int):
        self.titolo_film: str = titolo_film
        self.num_posti: int = num_posti


        for sala in self.sale:
            if sala.posti_disponibili() >= num_posti:
                print(f"{titolo_film.titolo}, sala numero: {sala.num_ident}, {num_posti} posti.")
            else:
                print(f"Per il film: {titolo_film.titolo} non ci sono posti disponibili.")


the_avengers: Film = Film('The Avengers', '2:33')
sala1: Sala = Sala(2, 5, 43, film_adesso=the_avengers)
cinema1: Cinema = Cinema([])
cinema1.aggiungi_sala(sala1)
cinema1.prenota_film(the_avengers, 3)