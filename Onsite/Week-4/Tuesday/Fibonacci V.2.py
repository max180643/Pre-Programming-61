"""Fibonacci V.2"""
def main(num=int(input())):
    """Main Function"""
    fib1, fib2 = 0, 1
    for _ in range(num):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1

print(main())
