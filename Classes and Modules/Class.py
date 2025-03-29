class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __repr__(self):
        print(f"{self.name}")
    
    def noise(self):
        print(f"{self.sound}")

Dog = Animal("Dog", "Bark")
Dog.noise()
