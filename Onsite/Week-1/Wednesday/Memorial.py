"""Memorial"""
import math
def main():
    """Main Function"""
    diameter = float(input())
    height = float(input())
    ans = (1 / 3) * math.pi * pow(diameter / 2, 2) * height
    print("%.3f"%(ans))

main()
