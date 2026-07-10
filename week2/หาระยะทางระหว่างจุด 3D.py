import math
"""ddddd"""
def main():
    """ddddd"""
    a = input()
    asplit = a.split(" ")
    b = input()
    bsplit = b.split(" ")

    x1 = int(asplit[0])
    y1 = int(asplit[1])
    z1 = int(asplit[2])
    x2 = int(bsplit[0])
    y2 = int(bsplit[1])
    z2 = int(bsplit[2])
    d = math.sqrt(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))
    print(f"{d:.2f}")
main()
