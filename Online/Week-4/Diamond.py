"""Diamond"""
def main():
    """Main Function"""
    number = int(input())
    for i in range(1, number + 1, 2):
        space = " " * int((number - i) / 2)
        asterisk = "*" * i
        print(space + asterisk)
    for j in range(number - 2, 0, -2):
        space = " " * int((number - j) / 2)
        asterisk = "*" * j
        print(space + asterisk)

main()
