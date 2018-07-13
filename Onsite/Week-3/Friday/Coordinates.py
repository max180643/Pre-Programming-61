"""Coordinates"""
def main():
    """Main Function"""
    text = input()
    text = text[1:-1]
    text = text.split(", ")
    print("x: %i" % (int(text[0])))
    print("y: %i" % (int(text[1])))

main()
