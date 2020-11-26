#create a program to display the path Beep and Bop are taking 
import matplotlib.pyplot as plt 

def small():

  # should display a small square using a line plot with a red dotted line
  x = [3,3,4,4,3]
  y = [3,4,4,3,3]
  plt.plot(x,y, 'r:o')

def medium():
  #should display a medium square with a green dashed line
  x = [2,2,5,5,2]
  y = [2,5,5,2,2]
  plt.plot(x, y, 'g--s')

def large():

  x = [1,1,6,6,1]
  y = [1,6,6,1,1]
  plt.plot(x ,y, 'b-s')

def run():
  small()
  medium()
  large()
  plt.show()
run()


