"""Milk"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
milk = 0
pro = 0
if not d :
    print(milk)
elif d > a and b != 0:
    milk = d//a
    pro = (milk//b) * c
    print(milk+pro)
elif d > a and b > c:
    milk = d//a
    print(milk)
elif d > a and (not b) :
    milk = d//a
    print(milk)