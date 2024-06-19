
class Media:

    def __init__(self):
        self.title: str = None
        self.reviews: int = []
    

    def set_title(self, title: str):
        self.title:str = title

    def get_title(self):
        
        return self.title


    def aggiungiValutazione(self, voto: int):
        self.voto: int = voto

        if voto in list(range(1,5)):
            self.reviews.append(voto)


    def getMedia(self):
        self.media: float = media

        for i in self.reviews:
            media = sum(self.reviews) / len(self.reviews)
            print(media)


    def getRate(self):

        media = self.getMedia()

        if media <= 1.5:
            print('Terribile')
        elif media > 1.5 and media <= 2.5:
            print('Brutto')
        elif media > 2.5 and media <= 3.5:
            print('Normale')
        elif media > 3.5 and media <= 4.5:
            print('Bello')
        else:
            print('Grandioso')


    def ratePercentage(self, voto: float):
        self.voto: float = voto

        return (voto / len(self.reviews)) * 100


    def recensione(self):

        print(f'Titolo film: {self.get_title()}\n'
              f'Voto medio: {self.getMedia()}\n'
              f'Giudizio: {self.getRate()}\n'
              f'Percentuale: {self.ratePercentage}')
             
