class Animal():

    zoo_name="Eram Zoo"

    def __init__(self,name,species,age,sound):
        self.name=name
        self.species=species
        self.age=age
        self.sound=sound

    def make_sound(self):
        return self.sound 

    def info(self):
        return  self.name,self.species ,self.age ,self.sound, Animal.zoo_name

    def __str__(self):
        return f"{self.name},{self.species} ,{self.age },{self.sound}, {Animal.zoo_name}" 
        

class bird (Animal):
    def __init__(self,name,species,age,sound,wing_span):

        super().__init__(name,species,age,sound)

        self.wing_span=wing_span

    def make_sound(self):
        return f"{self.name} sedash:{self.sound}"

    def info(self):
        return super().info()+(f"wing span :{self.wing_span}cm",)

        


shir=Animal("shir","pestandar",20,"ghoresh")

print(shir)

print(shir.make_sound())

print(shir.info())

parrot=bird("tuti","parrot",1,"jik_jik",23)

print(parrot)

print(parrot.make_sound())

print(parrot.info())

