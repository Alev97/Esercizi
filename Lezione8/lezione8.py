
class Animal:

    def __init__(self, name: str, species: str, age: int):

        self.species: str = species
        self.age: int = age
        self.age: int = name

    def speak(self) -> str:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name}, species={self.species}, age={self.age})'

class Person(Animal):

    def __init__(self, name: str, surname: str, cf: str, species: str, age: int):
        
        super().__init__(species, age)
        self.name: str = name
        self.surname: str = surname
        self.cf: str = cf

    def speak(self) -> str:
        return f'Ciao mi chiamo {self.name} {self.surname} e ho {self.age} anni.'
    
    def __str__(self) -> str:

        return f'{self.name.capitalize()} {self.surname.capitalize()}(cf={self.cf})'\
            + f', age={self.age})'\
            + f', species={self.species})'



class Cat(Animal):

    def __init__(self, name: str, age: int):

        super().__init__("Felidos", age)

    def speak(self) -> str:
        return 'Miao'
        

class Rabbit(Animal):

    def __init__(self, name: str, age: int):

        super().__init__(name, 'Leporide', age)

class Student(Person):

    def __init__(self, matricola: str):

        self.matricola = matricola


p = Person(name='Lorenzo', surname='Maggi', cf='bella', age=22)
a = Animal(name='Willy', species='Baleana Balena', age=22)
print(a.__class__.__name__)
c = Cat(name='Pippo', age=25)
print(c.__class__.__name__)
print(c)
print(c.speak())

# Esercizio 2

class Rooms:

    def __init__(self, id: str, floor: int, seats: int):
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats

    def get_floor(self) ->str:
        return self.floor
    
    def get_seats(self) ->str:
        return self.seats
    
    def get_id(self) -> str:
        return self.id

    def __str__(self) -> str:
        return f'Room(id={self.id}, floor={self.floor}, seats={self.seats})'



class Building:

    def __init__(self, name: str, address: str, num_floors: tuple[int, int]):
        
        self.name: str = name
        self.address: str = address
        self.num_floors: int = num_floors
        self.rooms: list[Rooms] = []

    def get_num_floors(self) ->str:
        return self.floor
    
    def get_rooms(self) ->list[Rooms]:
        return self.rooms
    
    def add_room(self, room: Rooms):
        if room and isinstance(room, Rooms) and room not in self.rooms\
            and room.get_floor() <= self.get_num_floors():
            self.rooms.append(room)

    def area(self)
    
    
    def __str__(self) -> str:
        s: str = f'{self.name} {self.address}\n'
        s += 'Which Rooms:\n'
        for room in self.get_rooms():
            s += room.__str__() + '\n'
        return s + f'Area = {self.area()}=2'
    
class Person:

    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age





class Group:

    def __init__(self, name: str, limit: int):
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []

    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> int:
        retunr self.limit

    def


class Course:

    def __init__  
    
smi = Building(name='SMI', address='Via Sierra Nevada 60', num_floors=5)


smi.add_room(Rooms(id='666', floor=3, seats=32))
smi.add_room(Rooms(id='333')





fullstack = Group(name='Fullstack', limit=30)
lorenzo = Student()