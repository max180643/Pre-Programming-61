"""Print i"""
def main():
    """Main Function"""
    check = input()
    start = int(input())
    end = int(input())
    if check == "Vertical":
        if start <= end:
            for i in range(start, end + 1):
                print("{:02}" .format(i))
        else:
            for i in range(start, end - 1, -1):
                print("{:02}" .format(i))
    elif check == "Horizontal":
        if start <= end:
            for i in range(start, end + 1):
                print("{:02} " .format(i), end="")
        else:
            for i in range(start, end - 1, -1):
                print("{:02} " .format(i), end="")

main()
