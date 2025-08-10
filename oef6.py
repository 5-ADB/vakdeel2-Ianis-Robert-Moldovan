import matplotlib.pyplot as plt

x = list(range(0, 11))
y = [2 * i for i in x]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()