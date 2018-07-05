"""Mirrored Slope"""
def main(number):
    """Main Function"""
    for i in range(number, 0, -1):
        print("%s/" % (" " * (i - 1)))

main(int(input()))
