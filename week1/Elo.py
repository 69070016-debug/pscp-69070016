"""elo"""
def main():
    """elo"""
    ra = int(input())
    rb = int(input())
    x = input()
    ea = 1 / (1+10**((rb-ra)/400))
    eb = 1 / (1+10**((ra-rb)/400))
    if x == "A":
        print(f"{ea:.2f}")
    elif x == "B":
        print(f"{eb:.2f}")
main()
