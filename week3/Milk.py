"""Milk"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
milk = d//a
cap = milk
if b > 0 and c > 0:
    while cap >= b:
        pro = (cap//b)*c
        milk += pro
        cap = (cap%b)+pro
    print(milk)
else:
    print(milk)
