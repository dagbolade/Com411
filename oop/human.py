class Human:

  #class attributes,  always constant
  MAX_ENERGY = 100

  #setting the initialiser
  def __init__(self, name = "David", age = 0, ):

    #instance attributes
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  def __str__(self):
   return f'My name is {self.__name} and I am {self.age} years old.'  

  # magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})' 

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  #Adding a method grow that increases the age of the object by 1  
  def grow(self):
    self.age += 1

  #adding a method eat that takes an amount as a parameter.  This should increase the energy of the object by the amount.  Note, energy should not exceed MAX_ENERGY
  def eat(self, amount):
    potential_energy = self.energy + amount

    if potential_energy > Human.MAX_ENERGY:
      self.energy = Human.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0  

  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0
    


 

if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))
    

