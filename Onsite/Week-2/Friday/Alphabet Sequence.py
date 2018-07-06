"""Alphabet Sequence"""
def main():
    """Main Function"""
    char = input()
    for i in range(ord("A"), ord(char) + 1):
        if (i >= 91 and i <= 96) or i > 122 or i < 65:
            print("", end="")
        else:
            print("%s" % (chr(i)), end="")

main()
