from inhabitant import Inhabitant

class Human(Inhabitant):

  #class attributes,  always constant
  MAX_ENERGY = 100

  #setting the initialiser
  def __init__(self, name = "David", age = 0, ):
    super().__init__(name, age)

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

 

 

if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))
    

