"""Vending Machine"""
def main():
    """Main Function"""
    money = 0
    item = 0
    total = 0
    while True:
        input_ = input()
        if input_ != "END":
            if int(input_) >= 0:
                money += int(input_)
            elif int(input_) < 0:
                item += 1
                total += abs(int(input_))
                if money - total < 0:
                    print("ERROR: Not enough money for this item.")
                    total -= abs(int(input_))
                    if item > 0:
                        item -= 1
        else:
            print("Items: %i" % (item))
            print("Change: %i THB" % (money - total))
            break

main()
