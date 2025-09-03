class Flyer:
    def __init__(self, name):
        self.name = name

class Swimmer:
    def __init__(self, name):
        self.name = name        

class Duck(Flyer,Swimmer):  
    def bark(self):
        print("Duck is flying Duck is swimming")



duck = Duck()
duck.fly()
duck.swim
print(duck)