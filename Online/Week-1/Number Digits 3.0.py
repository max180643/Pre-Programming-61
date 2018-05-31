"""Number Digits 3.0"""
def main():
    """Main Function"""
    set1 = int(input()) % 10                # Digit-5
    set2 = int(input()) % 100 // 10         # Digit-4
    set3 = int(input()) % 1000 // 100       # Digit-3
    set4 = int(input()) % 10000 // 1000     # Digit-2
    set5 = int(input()) % 100000 // 10000   # Digit-1
    total = set1 + set2 + set3 + set4 +set5
    print("%i+%i+%i+%i+%i = %i"%(set1, set2, set3, set4, set5, total))

main()
