"""find how many time we need to click on calculator"""
n = int(input())
if n == 1:
    print(1)
else:
    total_digits = 0
    for i in range(1, n + 1):
        total_digits += len(str(i))
    print(total_digits + n)
