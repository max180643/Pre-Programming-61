"""Arithmetic Sequence"""
def main():
    """Main Function"""
    frist = int(input())
    member = int(input())
    differ = int(input())
    if member > 0:
        i = 1
        print(frist, end=" ")
        while i < member:
            frist += differ
            print(frist, end=" ")
            i += 1
            range()

main()
