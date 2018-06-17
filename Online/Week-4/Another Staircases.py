"""Staircases"""
def main():
    """Main Function"""
    number = int(input())
    for i in range(number):
        space = " " * (number - 1 - i)
        stair = "*" * (i + 1)
        print(space + stair)

main()
