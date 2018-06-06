"""Newbie Encoder"""
def main():
    """Main Function"""
    text = ord(input())
    text = text - ((26 * ((text == 122) or (text == 90))) - 1)
    print(chr(text))

main()
