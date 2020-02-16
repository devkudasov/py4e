hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h < 40:
    print(h * r)
else:
    print(40 * r + (h - 40) * r * 1.5)
