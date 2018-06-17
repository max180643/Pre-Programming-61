"""Pyramid"""
def main():
    """Main Function"""
    number = int(input())
    for i in range(number):
        space = " " * (number - 1 - i)
        asterisk = "*" * (2 * i + 1)
        print(space + asterisk)

main()
