"""Greatest Common Divisor"""
def main():
    """Main Function"""
    in1 = int(input())
    in2 = int(input())
    num1 = min(in1, in2)
    num2 = max(in1, in2)
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            print(i)
            break

main()
