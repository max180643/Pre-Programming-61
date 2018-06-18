"""Alpha Signal"""
def main():
    """Main Function"""
    text = input().lower()
    for i in text:
        number = ord(i) - 96
        print(max(0, number) * "*")

main()
