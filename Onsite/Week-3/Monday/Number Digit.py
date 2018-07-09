"""Number Digit"""
def main():
    """Main Function"""
    number = abs(int(input()))
    number1 = str(number)
    digit = int(input())
    if digit <= 0:
        print("Index error.")
    elif digit > len(number1):
        print("Index out of range.")
    else:
        print(number1[len(number1) - digit])

main()
