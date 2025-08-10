def deel(a, b):
    try:
        resultaat = a / b
        print(f"Resultaat: {resultaat}")
    except ZeroDivisionError:
        print("Je kan niet delen door 0")

deel(10, 0)