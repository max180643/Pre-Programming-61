"""[Extra] Count Fast!"""
def main():
    """Main Function"""
    set1 = call(1, 2, 3, 4, 5)
    set2 = call(6, 7, 8, 9, 10)
    set3 = call(11, 12, 13, 14, 15)
    set4 = call(16, 17, 18, 19, 20)
    set5 = call(21, 22, 23, 24, 25)
    set6 = call(26, 27, 28, 29, 30)
    set7 = call(31, 32, 33, 34, 35)
    set8 = call(36, 37, 38, 39, 40)
    set9 = call(41, 42, 43, 44, 45)
    set10 = call(46, 47, 48, 49, 50)
    print(set1)
    print(set2)
    print(set3)
    print(set4)
    print(set5)
    print(set6)
    print(set7)
    print(set8)
    print(set9)
    print(set10)

def call(num1, num2, num3, num4, num5):
    """Call Name"""
    return "%s:%i#\t\t%s:%i#\t\t%s:%i#\t\t%s:%i#\t\t%s:%i#"\
    % (input(), num1, input(), num2, input(), num3, input(), num4, input(), num5)

main()
