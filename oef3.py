lijst = [10, 20, 30]

try:
    print(lijst[5])
except IndexError:
    print("Index bestaat niet in lijst")
    