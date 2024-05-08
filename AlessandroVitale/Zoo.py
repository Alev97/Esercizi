
class Zoo:

    def __init__(self, fences: str, zookepers: str):
        self.fences = fences
        self.zookepers = zookepers
        
class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health: float):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = health

class Fance:

    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

class ZooKeeper:

    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.username = surname
        self.id = id

        


