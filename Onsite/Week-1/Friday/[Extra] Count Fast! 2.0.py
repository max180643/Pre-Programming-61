"""[Extra] Count Fast!"""
def main():
    """Main Function"""
    set1 = call(0)
    set2 = call(5)
    set3 = call(10)
    set4 = call(15)
    set5 = call(20)
    set6 = call(25)
    set7 = call(30)
    set8 = call(35)
    set9 = call(40)
    set10 = call(45)
    print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s"\
     % (set1, set2, set3, set4, set5, set6, set7, set8, set9, set10))

def call(call):
    """Call Name"""
    return "%s:%i#\t\t%s:%i#\t\t%s:%i#\t\t%s:%i#\t\t%s:%i#"\
    % (input(), call + 1, input(), call + 2, input(), call + 3, input(), call + 4, input(), call + 5)

main()
