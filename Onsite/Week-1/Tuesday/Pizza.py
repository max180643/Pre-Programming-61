"""Pizza"""
def main():
    """Main Function"""
    total = int(input())
    size = int(input())
    box = total // size + (1 * (total % size > 0))
    print("%i"%(box))

main()
