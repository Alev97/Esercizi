
from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcella: float):
        super().__init__(first_name, last_name)

        if isinstance(specialization, str):
            self.__specialization = specialization
        else: 
            self.__specialization = None
            print('La specializzazione non è una stringa')

        if isinstance(parcella, float):
            self.__parcella = parcella
        else:
            self.__parcella = None
            print('La parcella non è un float')

    def setSpecialization(self, specialization: str):
        
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print('La specializzazione inserita non è una stringa!')

    def setParcel(self, parcella: float):
        
        if isinstance(parcella, float):
            self.__parcella = parcella
        else:
            print('La parcella inserita non è un float!')

    def getSpecialitation(self):

        return self.__specialization
    
    def getParcel(self):

        return self.__parcella
    
    def isAvalidDoctor(self):

        if self.__age > 30:
            print(f'Dottor {self.__first_name} {self.__last_name} is valid')
        else:
            print(f'Dottor {self.__first_name} {self.__last_name} is not valid')

    def doctorGreet(self):
        self.greet()

        print(f'Sono un medico {self.__specialization}')



