import matplotlib.pyplot as plt

def coordinate():
    print("please enter a value for your x")
    x = int(input())
    print("please enter a value for your y")
    y = int(input())
    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for values in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]
def run():
    values = path()
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(values[0], values[1], 'ro--')
    plt.show()
    
run()



