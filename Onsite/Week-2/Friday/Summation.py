"""Summation"""
def main():
    """Main Function"""
    num1 = int(input())
    total = 0
    for _ in range(num1):
        num2 = float(input())
        total += num2
    print("%.4f" % (total))

main()
