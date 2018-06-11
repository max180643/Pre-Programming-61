"""Intermediate Encoder"""
def main():
    """Main Function"""
    num = ord(input())
    if 64 < num < 71 or 96 < num < 103:
        num = num + 20
    else:
        num = num - 6
    print(chr(num))

main()
