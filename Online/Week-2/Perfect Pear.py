"""Perfect Pear"""
def main():
    """Main Function"""
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    print(val1 + val2 + val3 - min(val1, val2, val3) - max(val1, val2, val3))

main()
