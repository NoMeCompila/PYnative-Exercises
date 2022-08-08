
def list_float():

    try:
        l = []
        for i in range(5):
            x = float(input(f"enter a float number for {i+1} position: "))
            l.append(x)
        print(l)

    except ValueError:
        print("Invalid data please start again...")
        list_float()


list_float()