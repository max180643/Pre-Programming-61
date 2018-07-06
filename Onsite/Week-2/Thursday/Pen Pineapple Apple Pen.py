"""Pen Pineapple Apple Pen"""
def main():
    """Main Function"""
    check = 0
    while True:
        text = input()
        # input check
        if text == "Pen" and check == 0:
            check += 1
        elif text == "Pineapple" and check == 1:
            check += 1
        elif text == "Apple" and check == 2:
            check += 1
        elif text == "Pen" and check == 3:
            check += 1
        else:
            check = 0
            if text == "Pen":
                check = 1
            print("Wrong lyrics!")
        # value check
        if check == 4:
            print("Correct lyrics!")
            break

main()
