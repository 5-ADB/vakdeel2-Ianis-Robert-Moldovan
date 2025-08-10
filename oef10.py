import matplotlib.pyplot as plt
import random

x = [random.randint(1, 100) for _ in range(50)]
y = [i + random.randint(-10, 10) for i in x]

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
