import matplotlib.pyplot as plt

def combined():
    x = [3,5,7,3]
    y = [3,5,3,3]
    plt.plot(x,y,'r--o')

def t1():
    x = [3,5,7,3]
    y = [5,3,5,5]
    plt.plot(x,y,'b:s')

    ###
def t2():
    x = [3,3,7,3]
    y = [3,5,4,3]
    plt.plot(x,y,'g-*')

    ###
def t3():
    x = [7,7,3,7]
    y = [3,5,4,3]
    plt.plot(x,y,'y-p')

    #Show()
def run():
  combined()
  t1()
  t2()
  t3()
  plt.show()
  
run()
  
    
