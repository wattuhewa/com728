import matplotlib.pyplot as plt

x=[0,2,4,6,8,10,15]
y=[0,20,40,60,80,100,150]

plt.xlabel("x values")
plt.ylabel("y values")

plt.step(x,y)
plt.show()
