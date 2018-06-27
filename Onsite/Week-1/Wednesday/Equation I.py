"""Equation I"""
import math
def main():
    """Main Function"""
    number = float(input())
    ans = (2 * math.log10(number)) + (number / 3)
    print("%.2f"%(ans))

main()
