
# Esercizio 9-1 e 9-2

class Restaurant:

    def __init__(self, name: str, cuisine_type: str):
        self.name = name
        self.cuisine_type = cuisine_type

    def descibe_restaurant(self):
        print(f'Restaurant(name={self.name}, '\
              + f'cuisine={self.cuisine_type}')
        
    def open_restaurant(self):
        print(f'Il ristorante {self.name} è aperto')

r1 = Restaurant(name='La pergola', cuisine_type='Chic')
r1.descibe_restaurant()
r1.open_restaurant()
print('#' * 30)
r2 = Restaurant(name='La vecchia Roma', cuisine_type='Romana')
r2.descibe_restaurant()
r2.open_restaurant()
r3 = Restaurant(name='Fico Vecchio', cuisine_type='Mediterranea')
r3.descibe_restaurant()
r3.open_restaurant()

# Esercizio 9-3

'''
class User:

    def __init__()
'''       

# da finire

# Eseercizio 9-4

class Restaurant:

    def __init__(self, name: str, cuisine_type: str, number_served: int = 0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def descibe_restaurant(self):
        print(f'Restaurant(name={self.name}, '\
              + f'cuisine={self.cuisine_type}')

        
    def open_restaurant(self):
        print(f'Il ristorante {self.name} è aperto')

    
    def increment_number(self):
        self.number_served += 1
    

r1 = Restaurant(name='La vecchia Roma', cuisine_type='Romana')
print(r1.number_served)
#r1.set_number_served(2)
print(r1.number_served)
r1.increment_number()
print(r1.number_served)


# Esercizio di ripasso


from typing import Tuple

a: tuple = (1, 2)

class Persona:
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str,
                 genere: str,
                 codice_fiscale: str) -> None:
        
        self.nome: str = name
        self.cognome: str = cognome
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere
        self.codice_fiscale: str = codice_fiscale
        
    def calcola_eta(self)->int:
        
        return 10
    
    def __eq__(self, value: object) -> bool:

        return value.codice_fiscale == self.codice_fiscale
    
    __eq__(persona_1, persona_2)
    persona_1 == Persona_2
    
    
    persona_1: Persona = Persona(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio")


class Dipendente(Persona):
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str,
                 ore_lavorate: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere)
        self.ore_lavorate: int = ore_lavorate

        
    def calcola_stipendio(self)->float:
        
        return 500.0

    def __str__(self) -> str:
        return super().__str__()
    
    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)


dipendente_1: Dipendente = Dipendente(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio",
                             ore_lavorate=500)



class Professore(Dipendente):
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str, 
                 ore_lavorate: int,
                 materia_insegnata: str,
                 ore_di_lezione: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)
        
        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione
        
    def __str__(self) -> str:
        return f'Professor {self.nome} {self.cognome}

    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)
    

print(persona_1.calcola_eta())

print(dipendente_1.ore_lavorate)
print(dipendente_1.nome)
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())



professore_1: Professore = Professore(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio",
                             ore_lavorate=500,
                             materia_insegnata="Python",
                             ore_di_lezione=1000)

print(professore_1.ore_di_lezione)

print(str())

