"""The Camp EP.4"""
def main():
    """Main Fucntion"""
    text = input()
    text = text.split(" ")
    text2 = text[1]
    text3 = text2[0]
    print("{}. {}" .format(text3, text[0]))

main()
