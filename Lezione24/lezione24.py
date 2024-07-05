
class Documento:

    def __init__(self, testo: str):
        self.testo: str = testo

    def getText(self):

        return self.testo
    
    def setText(self, testo: str):
        self.testo: str = testo

    def isInText(self, parola_chiave: str):
        self.parola_chiave: str = parola_chiave

        if parola_chiave in self.testo:

            return True
        
        else:

            return False
        
class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo_mes: str):
        super().__init__(testo)
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo_mes: str = titolo_mes

    def getMittiente(self):

        return self.mittente
    
    def setMittente(self, mittente: str):
        self.mittente: str = mittente

    def getDestinatario(self):

        return self.destinatario
    
    def setDestinatario(self, desrinatario: str):
        self.destinatario: str = desrinatario

    def getTitoloMes(self):

        return self.titolo_mes
    
    def setTitoloMes(self, titolo_mes: str):
        self.titolo_mes: str = titolo_mes

    def getText(self):

        return f"Da: {self.mittente}\nTitolo: {self.titolo_mes}\nMessaggio: {self.testo}"
             
        
    






