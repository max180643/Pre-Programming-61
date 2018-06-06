"""Motion"""
import math
def main():
    """Main Function"""
    speed = int(input())
    degrees = int(input())
    line = degrees * (math.pi / 180)
    time = (((2 * speed) * (math.sin(line))) / 9.8)
    high = (((speed ** 2) * (math.sin(line) ** 2)) / (2 * 9.8))
    length = ((speed ** 2) * (math.sin((2 * line))) / 9.8)
    print("t = %.2f"%(time))
    print("H = %.2f"%(high))
    print("R = %.2f"%(length))

main()
