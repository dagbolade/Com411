



class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  def eat(self, amount):
    potential_energy = self.energy + amount

    if potential_energy > Inhabitant.MAX_ENERGY:
      self.energy = Inhabitant.MAX_ENERGY
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
    
  