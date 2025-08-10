import matplotlib.pyplot as plt

activiteiten = ["Studeren", "Sport", "Slapen", "Vrije tijd"]
uren = [5, 2, 8, 9]

plt.pie(uren, labels=activiteiten, autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.show()