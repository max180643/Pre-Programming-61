"""Cards Shuffling"""
def main():
    """Main Function"""
    total = 1
    check = True
    amount = int(input())
    if amount <= 0:
        print("0")
    elif amount == 1:
        card1 = int(input())
        print("0")
    else:
        card1 = int(input())
        for _ in range(amount - 1):
            card2 = int(input())
            if card2 >= card1 and check:
                total = total + 1
                card1 = card2
            else:
                check = False
        print(amount - total)

main()
