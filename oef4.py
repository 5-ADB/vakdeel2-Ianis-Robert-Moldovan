persoon = {"naam": "Ali", "leeftijd": 30}

try:
    print(persoon["adres"])
except KeyError:
    print("Adres bestaat niet in persoon")
