"""abcd"""
def main():
    """abcd"""
    num = input()
    a = input()
    num2 = num[::-1]
    num2 = int(num2)
    num = int(num)
    b = 0
    if a == "+":
        b = num+num2
    else:
        b = num*num2
    print(f"{num} {a} {num2} = {b}")
main()
