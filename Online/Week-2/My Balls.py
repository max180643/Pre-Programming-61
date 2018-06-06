"""My Balls"""
import math
def main():
    """Main Function"""
    radius = (float(input()) / 2)
    area = 4 * math.pi * math.pow(radius, 2)
    volume = (4/3) * math.pi * math.pow(radius, 3)
    print("A = %.3f"%(area))
    print("V = %.3f"%(volume))

main()
