import matplotlib.pyplot as plt

def read_data(filename):
  with open(filename) as file:
      temps = []
      for line in file:
        temperature = float(line.strip())
        temps.append(temperature)
  return temps      
      

  

def run():
  data = read_data("visual/plots/subplots/temps.txt")
  fig, axs = plt.subplots(1, 2)
  x = range(1,8)
  y = data
  
  plt.plot(x,y)
  plt.bar(x,y)
  plt.show()
run()  

