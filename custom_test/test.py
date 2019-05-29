li = [7, -8, 5, 4, 0, -2, -5]

a = sorted(li, key=lambda x: (x < 0, abs(x)))
# (x<0, x)
