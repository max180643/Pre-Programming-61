"""Power of X"""
def main():
    """Main Function"""
    width = int(input())
    for i in range(width):
        for j in range(width):
            if j == i:
                print("\\", end='')
            elif j == width - i -1:
                print("/", end='')
            else:
                print(" ", end='')
        print()

main()