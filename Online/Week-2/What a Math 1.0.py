"""What a Math"""
import math
def main():
    """Main Function"""
    x = float(input())
    a = float(input())
    y = (x * math.cos(math.radians(a))) - math.sqrt((math.pow(a,3) + math.sqrt((a * math.sin(math.radians(60)) + math.sqrt(a)))))
    print(int(((y > 0) * (-1 * (y * 2))) + y))

main()
