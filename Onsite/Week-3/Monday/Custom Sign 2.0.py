"""Custom Sign"""
def main():
    """Main Function"""
    size = int(input())
    text = input()
    text1 = text[:size - 2]
    align = input()
    if align == "Left":
        print("*" * size)
        print("*%s*" % (" " * (size - 2)))
        print("*%s*" % (text1.ljust(size - 2)))
        print("*%s*" % (" " * (size - 2)))
        print("*" * size)
    elif align == "Center":
        if (size - 2 - len(text)) % 2 == 0: # เลขคู่
            print("*" * size)
            print("*%s*" % (" " * (size - 2)))
            print("*%s*" % (text1.center(size - 2)))
            print("*%s*" % (" " * (size - 2)))
            print("*" * size)
        else: # เลขคี่
            print("*" * size)
            print("*%s*" % (" " * (size - 2)))
            print("* %s*" % (text1.center(size - 3)))
            print("*%s*" % (" " * (size - 2)))
            print("*" * size)
    elif align == "Right":
        print("*" * size)
        print("*%s*" % (" " * (size - 2)))
        print("*%s*" % (text1.rjust(size - 2)))
        print("*%s*" % (" " * (size - 2)))
        print("*" * size)

main()
