import matplotlib.pyplot as plt

x=[0, 5, 6, 10, 12, 20]
y=[0, 10, 30, 45, 5, 60]

plt.xlabel("time")
plt.ylabel("Distance")

plt.plot(x,y, "x")
plt.show()