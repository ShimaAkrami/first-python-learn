class Animal():
    def __init__(self,name,species,age,sound,zoo_name):
        self.name=name
        self.species=species
        self.age=age
        self.sound=sound
        self.zoo_name=zoo_name
    def make_sound(self):
        return self.sound
    def info(self):
        return  shir.name,shir.species ,shir.age ,shir.sound, shir.zoo_name
    def __str__(self):
        r=print(f"{self.name},{self.species} ,{self.age },{self.sound}, {self.zoo_name}")  
        return r

class bird (Animal):
    def __init__(self,name,species,age,sound,zoo_name,wing_span):
        Animal.__init__(self,name,species,age,sound,zoo_name)
        self.wing_span=wing_span
    def make_sound(self):
        return self.sound

        


shir=Animal("shir","pestandar",20,"ghoresh","eram")

print(shir.name,shir.species ,shir.age ,shir.sound, shir.zoo_name)

print(shir.make_sound())

print(shir.info())

print(shir)