"""Holynum"""
def main():
    """Main Function"""
    number = int(input())
    digit = int(input())
    if digit == 0:
        print(number)
    elif digit == 1:
        print(number - (number % 10))
    elif digit == 2:
        print(number - (number % 100))
    elif digit == 3:
        print(number - (number % 1000))
    elif digit == 4:
        print(number - (number % 10000))
    elif digit == 5:
        print(number - (number % 100000))
    elif digit == 6:
        print(number - (number % 1000000))
    elif digit == 7:
        print(number - (number % 10000000))
    elif digit == 8:
        print(number - (number % 100000000))
    elif digit == 9:
        print(number - (number % 1000000000))

main()
