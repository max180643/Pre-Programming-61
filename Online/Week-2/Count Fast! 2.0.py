"""Count Fast!"""
def main():
    """Main Function"""
    set1 = call(0) + call(1) + call(2) + call(3) + call(4)
    set2 = call(5) + call(6) + call(7) + call(8) + call(9)
    set3 = call(10) + call(11) + call(12) + call(13) + call(14)
    set4 = call(15) + call(16) + call(17) + call(18) + call(19)
    set5 = call(20) + call(21) + call(22) + call(23) + call(24)
    set6 = call(25) + call(26) + call(27) + call(28) + call(29)
    set7 = call(30) + call(31) + call(32) + call(33) + call(34)
    set8 = call(35) + call(36) + call(37) + call(38) + call(39)
    set9 = call(40) + call(41) + call(42) + call(43) + call(44)
    set10 = call(45) + call(46) + call(47) + call(48) + call(49)
    print(set1 + "\n" + set2 + "\n" + set3 + "\n" + set4 + "\n" + set5)
    print(set6 + "\n" + set7 + "\n" + set8 + "\n" + set9 + "\n" + set10)

def call(num):
    """Call Name"""
    name = str(input())
    num = num+1
    return name + ":" + str(num) + "#\t\t"

main()
