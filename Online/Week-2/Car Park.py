"""Car Park"""
def main():
    """Main Function"""
    set1 = info(1) + info(2) + info(3) + info(4) + info(5)
    set2 = info(6) + info(7) + info(8) + info(9) + info(10)
    set3 = info(11) + info(12) + info(13) + info(14) + info(15)
    set4 = info(16) + info(17) + info(18) + info(19) + info(20)
    print(set1 + set2 + set3 + set4)
def info(num):
    """Car Info"""
    price = int(input())
    time = float(input())
    time = int(time)
    total = price * time
    return "Car No.%02i: %.2f Baht.\n"%(num, total)

main()
