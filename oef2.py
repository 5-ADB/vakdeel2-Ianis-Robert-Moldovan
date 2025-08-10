def tel_op(a, b):
    try:
        return a + b
    except TypeError:
        print("Je kan geen worden met cijfers optellen")

tel_op(5, "drie")