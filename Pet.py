#Class definition
class Pet:
    def __init__(self, name):
#instance attributes
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} enjoyed their meal!")
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a refreshing nap!")
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} had fun playing!")
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")
    def show_tricks(self):
        if self.tricks:
            print(f"\n{self.name}'s Tricks")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
    def get_status(self):
        print(f"\n{self.name}'s Status")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


my_pet = Pet("Buddy") #Class object creation
my_pet.get_status()

my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.get_status()

my_pet.train("Sit")
my_pet.train("Fetch")
my_pet.show_tricks()
my_pet.train("Sit") # Trying to teach a trick already learned

my_pet.play()
my_pet.get_status()        
