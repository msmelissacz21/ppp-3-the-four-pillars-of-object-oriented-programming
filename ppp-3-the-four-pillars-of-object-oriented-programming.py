from unicodedata import name


class Person:
  def __init__(self,in_name,in_age):
    self.name = in_name
    self.age = in_age
      
  def get_name(self):
    return self.name

class Zoo:
  def __init__(self,name="Local Zoo"):
    self.name = name
    self.animals = []
    self.customers = []

  def add_animal(self, animal):
    self.animals.append(animal)
    print(f"{self.name} has a(n) {animal}")
  
  def add_animals(self, animals):
    self.animals.extend(animals)
    print(f"{self.name} has many animals")
  
  def add_customer(self, name):
    self.customers.append(name)
    print(f"{name} has entered {self.name}")

  def remove_customer(self, name):
    self.customers.remove(name)
    print(f"{name} has left {self.name}")
  
  def visit_animals(self):
    for a in self.animals:
      print(f"visiting {a.get_name()}")
      a.make_noise()
      a.eat_food()

class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return self.name
  def make_noise(self):
    print("Every animal makes noise")
  def eat_food(self):
    print("All creatures need sustenance")

class Fish(Animal):
    def __init__(self, name):
        super(Fish, self).__init__(name)

    def eat_food(self):
       print("I eat pellets")

    def make_noise(self):
       return print("bloop")

class Bird(Animal):
    def __init__(self, name):
        super(Bird, self).__init__(name)

    def eat_food(self):
       print("I eat seeds")

    def make_noise(self):
       return print("I chirp")

class Chimp(Animal):
    def __init__(self, name):
        super(Chimp, self).__init__(name)

    def eat_food(self):
       print("I eat bananas")

    def make_noise(self):
       return print("AHHHHH!")

f = Fish('larry')
f.eat_food()
f.make_noise()

a = Chimp('Zoe')
a.eat_food()
a.make_noise()



class Customer:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        self.ticket = False
        self.in_zoo = False
        
    def buy_ticket(self):
        self.ticket = True

    def enter_zoo(self):
        self.in_zoo = False

    def exit_zoo(self):
        self.in_zoo = False

customer1 = Customer('Melissa',27)


print(customer1.ticket)

customer1.buy_ticket()

print(customer1.ticket)
