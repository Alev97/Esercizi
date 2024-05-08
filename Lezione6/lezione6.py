
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
r1.set_number_served(2)
print(r1.number_served)
r1.increment_number()
print(r1.number_served)
