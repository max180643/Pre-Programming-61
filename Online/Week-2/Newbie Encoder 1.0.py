"""Newbie Encoder"""
def main():
    """Main Function"""
    text = input()
    text = ord(text)
    rule = text == 122 or text == 90
    # rule = rule * 26
    text = text + 1 - (rule * 26)
    text = chr(text)
    print(text)

main()
