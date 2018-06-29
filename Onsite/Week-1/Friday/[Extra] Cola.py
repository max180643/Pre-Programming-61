"""[Extra] Cola"""
import math as m
def main():
    """Main Function"""
    can1 = convert(float(input()), float(input()))
    can2 = convert(float(input()), float(input()))
    can3 = convert(float(input()), float(input()))
    can4 = convert(float(input()), float(input()))
    can5 = convert(float(input()), float(input()))
    total = can1 + can2 + can3 + can4 + can5
    print("Total %.2f ml." % (total))

def convert(radiaus, height):
    """Convert"""
    return m.pi * radiaus ** 2 * height

main()
