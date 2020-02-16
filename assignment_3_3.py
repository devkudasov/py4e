rate = input("Enter rate (from 0 to 1)")

try:
    r = float(rate)
except:
    print("Enter number please")
    quit()

if r < 0 or r > 1:
    print("Number should be between 0 and 1")
elif r > 0.9:
    print("A")
elif r > 0.8:
    print("B")
elif r > 0.7:
    print("C")
elif r > 0.6:
    print("D")
else:
    print("F")
