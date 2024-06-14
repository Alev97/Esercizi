
from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, id_code: str):
        super().__init__(first_name, last_name)
        self.__id_code = id_code 

    def setIdCode(self, id_code: str):
        
        self.__id_code = id_code

    def getidCode(self):

        return self.__id_code
    
    def patientInfo(self):

        print(f"Paziente: {self.__first_name} {self.__last_name}\n"
              f"ID: {self.__id_code}")
