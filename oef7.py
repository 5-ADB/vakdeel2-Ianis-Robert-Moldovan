import matplotlib.pyplot as plt

x = list(range(0, 11))
y1 = x
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = x²")
plt.plot(x, y3, label="y = x³")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()