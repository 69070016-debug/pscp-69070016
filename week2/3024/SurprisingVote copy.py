"""abc"""
total = float(input())
maxx = float(input())
x = total - (maxx*2)
if x < 0:
    x = 0
if maxx - x > 2:
    print("Surprising")
else:
    print("Not surprising")
