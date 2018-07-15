"""Fibonacci 2.0"""
def main():
    """Main Function"""
    num = int(input())
    fib = [0, 1]
    for _ in range(2, num + 1):
        fib.append(fib[-1] + fib[-2])
    print(fib[num])

main()
