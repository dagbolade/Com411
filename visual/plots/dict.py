import matplotlib.pyplot as plt
import random

def data():
  paths = {}
  print("What type of line would you like(:, -- or -)")
  user = input()
  print("what colour they would like (r, g or b)")
  userr = input()
  print("what style of marker they would like (o, s or ^)")
  useer = input()
  
  #store the line style, colour, marker style in the dictionary as key-value pairs
  paths['line_style'] = user
  paths['colour'] = userr
  paths['marker_style'] = useer

  return paths

def generate():
  print("How many lines would you like to display?")
  no_of_lines = int(input())

  for lines in range(no_of_lines):
    values = data()
    #Generate 5 random numbers between 1 and 10
    x = random.sample(range(1, 10), 5)
    y = random.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line_style']}{values['marker_style']}"

    plt.plot(x, y, format)
  plt.show()

def run():
  print("Running...")
  generate()

  print("Done.")

run()








