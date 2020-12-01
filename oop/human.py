class Human:

  #class attributes,  always constant
  MAX_ENERGY = 100

  #setting the initialiser
  def __init__(self):

    #instance attributes
    self.name = "David"
    self.age = 0
    self.energy = Human.MAX_ENERGY
    

  # An instance method
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human()
  human.display()       
