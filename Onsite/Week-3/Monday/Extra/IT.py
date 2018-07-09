"""IT"""
def main():
    """Main Function"""
    num = int(input())
    print("%s%s%s\n" % ("***" * num, " " * num, "***" * num) * num, end="")
    print("%s%s%s%s%s%s\n" % (" " * num, "*" * num, " " * num, " " * num, " " * num, "*" * num)\
     * (num + num), end="")
    print("%s%s%s%s\n" % ("***" * num, " " * num, " " * num, "*" * num) * num, end="")

main()
