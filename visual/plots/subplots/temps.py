import matplotlib.pyplot as plt

def read_data(filename):
  with open(filename) as file:
      temps = []
      for line in file:
        temperature = float(line.strip())
        temps.append(temperature)
  return temps      
      

  

#def run():
  #data = read_data("visual/plots/subplots/temps.txt")
#  fig, axs = plt.subplots(2, 2)
 # x = range(0,7)
 # y = data
 # print(x,y)
  
 # plt.plot(x,y, 'r')
 # plt.bar(x,y)
  #plt.show()
#run()  

def run():
  data = read_data('visual/plots/subplots/temps.txt')
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  plt.show()

run()