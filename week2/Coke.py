"""Coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
price = 0
if not b:
    price = a * d
else:
    for i in range(1, d+1):
        if not i % b:
            price += c
        else:
            price += a
print(price)
