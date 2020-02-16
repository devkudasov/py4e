hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)


def computepay(h, r):
    if h < 40:
        return h * r
    else:
        return 40 * r + (h - 40) * r * 1.5


print("Pay", computepay(h, r))
