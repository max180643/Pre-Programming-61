"""More Split Function"""
import math as m
def main():
    """Main Function"""
    number = float(input())
    if number <= 0:
        print("%.2f" % (abs(number) ** ((-1 / 2) * number)))
    elif 0 < number <= 2:
        print("%.2f" % (12 * m.pi * number))
    elif number > 2:
        print("%.2f" % ((((2 ** number) * m.sin(m.radians(number))) + m.sqrt(number)) / 2))

main()
