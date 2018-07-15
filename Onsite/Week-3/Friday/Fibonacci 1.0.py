"""Fibonacci"""
import math as m
def main():
    """Main Function"""
    print(int(fib(int(input()))))

def fib(num):
    """Fibonacci Cal"""
    return ((1 + m.sqrt(5)) ** num - (1 - m.sqrt(5)) ** num) / (2 ** num * m.sqrt(5))

main()
