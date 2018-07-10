"""Where is O?"""
def main():
    """Main Function"""
    text = input().lower()
    text = text.find("o")
    if text == -1:
        print("There is no O here")
    else:
        print("O is at %i" % (text + 1))

main()
