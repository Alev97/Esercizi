
from dottore import Dottore
from paziente import Paziente


class Fattura:

    def __init__(self, doctor: Dottore, patient: str = [Paziente]):
        self.doctor = doctor
        self.patient = patient
        self.fatture = None

        if doctor.isAvalidDoctor() == True:
            self.__fatture = len(list(patient))
            self.__salary = 0
        else:
            self.doctor: Dottore = None
            self.patient: list[Paziente] = None
            self.__fatture = None
            self.__salary = None

            print('Non è possibile creare la classe fattura poichè il dottore non è valido!')
            
            

        

        


