"""Pancake Shop EP.4"""
def main():
    """Main Function"""
    text = int(input())
    print("|------|")
    print("|{:<6}|" .format(text))
    print("|------|")
    print("")
    print("|------|")
    print("|{:>6}|" .format(text))
    print("|------|")
    print("")
    print("|------|")
    print("|{:>06}|" .format(text))
    print("|------|")

main()
