"""Balloon Game"""
def main():
    """Main Function"""
    set1 = balloon(int(input()), "P'Jack")
    set2 = balloon(int(input()), "P'Rew")
    set3 = balloon(int(input()), "P'Pok")
    set4 = balloon(int(input()), "P'Fight")
    set5 = balloon(int(input()), "P'Jub")
    print("%s\n%s\n%s\n%s\n%s"%(set1, set2, set3, set4, set5))

def balloon(score, name):
    """Score Check"""
    if score == 10:
        return "%s won a large teddy bear."%(name)
    elif score == 9 or score == 8:
        return "%s won a teddy bear."%(name)
    elif score == 7 or score == 6:
        return "%s won a key chain."%(name)
    elif score == 5 or score == 4:
        return "%s won a notebook."%(name)
    elif score == 3 or score == 2 or score == 1:
        return "%s won a pen."%(name)
    else:
        return "%s won nothing."%(name)

main()
