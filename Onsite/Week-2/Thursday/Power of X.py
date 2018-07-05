"""Power of X"""
def main():
    """Main Function"""
    number = int(input())
    for i in range(int(number / 2), 0, -1):
        print("\%s/" % (" " * i))


main()
