
from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testoInChiaro: str):

        self.testoInChiaro: str = testoInChiaro

        return testoInChiaro
    
class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato: str):

        self.testoCodificato: str = testoCodificato

        return testoCodificato
    
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int):

        self.chive: int = chiave

    
    def codifica(self, testoInChiaro: str):
        
        self.testoInChiaro: str = testoInChiaro






        
        
    
    
