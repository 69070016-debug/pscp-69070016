"""calculate buffet promotion"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())
price = 0
if z < x:
    price = a*z
elif z >= x:
    price = (((z//x)*y)*a)+((z%x)*a)
print(price)
