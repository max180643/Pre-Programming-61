""" The Camp EP.2 "Pick Day Pick Me Up!" """
def main():
    """Main Function"""
    day = int(input())
    if day >= 23 and day <= 25:
        print("Yep! %i UNiTEC@MP3" % (day))
    elif day > 31:
        print("404 NOT FOUND")
    else:
        print("Try again!")

main()
