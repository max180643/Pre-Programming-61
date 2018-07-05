"""Empty Box"""
def main(num):
    """Main Function"""
    for i in range(1, num + 1): # row
        for j in range(1, num + 1): # column
            if i == 1 or i == num or j == 1 or j == num:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

main(int(input()))
