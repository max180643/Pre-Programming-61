"""JOJO"""
def main():
    """Main Function"""
    text = input().upper().split(" ")
    dio = text.count("MUDA")
    jojo = text.count("ORA")
    if dio > 0:
        print("%s" % ("MUDA " * dio))
    if jojo > 0:
        print("%s" % ("ORA " * jojo))
    if dio > jojo:
        print("GOODBYE JOJO!")
    elif jojo > dio:
        print("Yare Yare Daze")
    elif dio == 0 and jojo == 0:
        print("Menacing")
    elif jojo == dio:
        print("WR%s" % ("Y" * dio))

main()
