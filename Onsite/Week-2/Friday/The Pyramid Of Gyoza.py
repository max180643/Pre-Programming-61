"""The Pyramid Of Gyoza"""
def main():
    """Main Function"""
    num = int(input())
    for i in range(0, num * 2, 2):
        print("%s%s" % (" " * (num - 1), "*" * (i + 1)))
        num -= 1

main()
