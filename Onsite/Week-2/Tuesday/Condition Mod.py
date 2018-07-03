"""Condition Mod"""
def main():
    """Main Function"""
    number = int(input())
    if number % 2 == 1:
        print("Oooo")
    elif number % 2 == 0 and 2 <= number <= 5:
        print("lelelel")
    elif number % 2 == 0 and 6 <= number <= 20:
        print("OMG!")
    elif number % 2 == 0 and number > 20:
        print("Infinite!")
    else:
        print("Out of condition!")

main()
