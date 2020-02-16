max = None
min = None

while True:
    str = input("Enter number")

    if str == "done":
        break

    try:
        num = int(str)

        if max is None and min is None:
            max = num
            min = num
        elif num < min:
            min = num
        elif num > max:
            max = num
    except:
        print("Invalid input")

print("Maximum is", max)
print("Minimum is", min)
