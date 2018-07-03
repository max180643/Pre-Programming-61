"""Basic Split Function"""
def main():
    """Main Function"""
    number = float(input())
    if number < 0:
        print("%.2f" % (pow(number, 2)))
    elif number == 0:
        print("%.2f" % (0))
    elif number > 0:
        print("%.2f" % (2 * number + 10))

main()
