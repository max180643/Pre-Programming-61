"""[Extra] Count Fast!"""
def main():
    """Main Function"""
    num = 0
    set1 = call(num)
    set2 = call(set1)
    set3 = call(set2)
    set4 = call(set3)
    set5 = call(set4)
    set6 = call(set5)
    set7 = call(set6)
    set8 = call(set7)
    set9 = call(set8)
    set10 = call(set9)

def call(num):
    """Call Name"""
    print("%s:%i#\t\t%s:%i#\t\t%s:%i#\t\t%s:%i#\t\t%s:%i#"\
    % (input(), num + 1, input(), num + 2, input(), num + 3, input(), num + 4, input(), num + 5))
    return num + 5

main()
