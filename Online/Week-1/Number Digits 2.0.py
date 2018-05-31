"""Number Digits"""
def main():
    """Main Function"""
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())
    int4 = int(input())
    int5 = int(input())

    set1 = int1 - ((int(int1 / 10)) * 10)
    set2 = int((int2 - ((int(int2 / 100)) * 100)) / 10)
    set3 = int((int3 - ((int(int3 / 1000)) * 1000)) / 100)
    set4 = int((int4 - ((int(int4 / 10000)) * 10000)) / 1000)
    set5 = int((int5 - ((int(int5 / 100000)) * 100000)) / 10000)

    total = (set1 + set2 + set3 + set4 +set5)
    print("%i+%i+%i+%i+%i = %i"%(set1, set2, set3, set4, set5, total))

main()
# Can Use // and % to find digits
