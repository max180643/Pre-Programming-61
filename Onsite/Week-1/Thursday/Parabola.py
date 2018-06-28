"""Parabola"""
def main():
    """Main Function"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    print("%.2f" % (parabola(num1)))
    print("%.2f" % (parabola(num2)))
    print("%.2f" % (parabola(num3)))
    print("%.2f" % (parabola(num4)))
    print("%.2f" % (parabola(num5)))

def parabola(num):
    """Parabola"""
    ans = ((1 / 25) * num ** 2) - ((6 / 5) * num) + 9
    return ans

main()
