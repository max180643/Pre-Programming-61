"""The Edge"""
def main():
    """Main Function"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    total = num1 + num2 + num3 + num4 + num5
    maximum = max(num1, num2, num3, num4, num5)
    minimum = min(num1, num2, num3, num4, num5)
    avg = total / 5
    print("Total: %.2f THB" % (total))
    print("Maximum: %.2f THB" % (maximum))
    print("Minimum: %.2f THB" % (minimum))
    print("Average: %.2f THB" % (avg))

main()
