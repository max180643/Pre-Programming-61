"""Bon Appetit"""
def main():
    """Main Function"""
    chilli = int(input())
    degree = input()
    order = int(input())
    # degree check
    if degree == "MILD":
        degree = 1000
    elif degree == "MEDIUM":
        degree = 2000
    elif degree == "SPICY":
        degree = 3000
    # check total
    if chilli - (degree * order) >= 0:
        print("Enough")
        print(chilli - (degree * order))
    else:
        print("Not Enough")

main()
