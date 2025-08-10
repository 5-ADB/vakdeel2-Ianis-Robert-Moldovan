import matplotlib.pyplot as plt
from collections import Counter

woord = "matplotlib"
frequentie = Counter(woord)

plt.bar(frequentie.keys(), frequentie.values())
plt.xlabel("Letter")
plt.ylabel("Frequentie")
plt.show()