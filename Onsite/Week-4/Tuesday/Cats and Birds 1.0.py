"""Cats and Birds"""
def main():
    """Main Function"""
    num = int(input())
    leg = int(input())
    # x + y = num
    # 2x + 4y = leg
    cat = (leg - (2 * num)) / 2
    bird = num - cat
    if cat % 1 == 0 and bird % 1 == 0:
        if cat >= 0 and bird >= 0:
            print(int(cat))
            print(int(bird))
        else:
            print("Impossible")
    else:
        print("Impossible")

main()
