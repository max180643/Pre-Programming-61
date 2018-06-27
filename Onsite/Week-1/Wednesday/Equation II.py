"""Equation II"""
import math
def main():
    """Main Function"""
    number = int(input())
    ans = math.sin(3 * math.radians(number)) + abs(number / 4) + 5
    print("%.2f"%(ans))

main()
