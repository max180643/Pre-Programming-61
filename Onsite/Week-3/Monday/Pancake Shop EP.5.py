"""Pancake Shop EP.5"""
def main():
    """Main Function"""
    text = float(input())
    print("|--------|")
    print("|{:<8.2f}|" .format(text))
    print("|--------|")
    print("")
    print("|--------|")
    print("|{:>8.2f}|" .format(text))
    print("|--------|")
    print("")
    print("|--------|")
    print("|{:>08.2f}|" .format(text))
    print("|--------|")

main()
