import matplotlib.pyplot as plt

def display(x,y):
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(x,y)
    plt.show()

def run():
    x_value=[1,2,3,4,5]
    y_value=[1,4,9,16,25]
    display(x_value,y_value)

run()
