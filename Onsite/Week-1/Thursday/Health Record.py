"""Health Record"""
def main():
    """Main Function"""
    set1 = (info(1, input(), int(input()), int(input()), int(input())))
    set2 = (info(2, input(), int(input()), int(input()), int(input())))
    set3 = (info(3, input(), int(input()), int(input()), int(input())))
    set4 = (info(4, input(), int(input()), int(input()), int(input())))
    set5 = (info(5, input(), int(input()), int(input()), int(input())))
    print(set1, set2, set3, set4, set5, sep="\n")

def info(number, name, day, month, year):
    """Information"""
    return "** Patient No.%i **\nFull Name: %s\nBirthday:  %i/%i/%i\n"\
           % (number, name, day, month, year)

main()
