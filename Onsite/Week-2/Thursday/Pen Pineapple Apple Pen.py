"""Pen Pineapple Apple Pen"""
def main():
    """Main Function"""
    while True:
        text = input()
        if text == "Pen":
            text = input()
            if text == "Pineapple":
                text = input()
                if text == "Apple":
                    text = input()
                    if text == "Pen":
                        print("Correct lyrics!")
                        break
        print("Wrong lyrics!")

main()
