"""Conversion of scales of temperature"""
temp = float(input())
t1 = input()
t2 = input()
if t1 == "K":
    c = temp-273.15
elif t1 == "F":
    c = (temp-32)*5/9
elif t1 == "R":
    c = temp*5/9
    c = c-273.15
elif t1 == "C":
    c = temp
t3 = 0
if t2 == "K":
    t3 = c+273.15
elif t2 == "F":
    t3 = c*9/5+32
elif t2 == "R":
    t3 = (c+273.15)*(9/5)
elif t2 == "C":
    t3 = c
print(f"{t3:.2f}")
