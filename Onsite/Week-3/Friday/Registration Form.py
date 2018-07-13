"""Registration Form"""
def main():
    """Main Function"""
    text = input()
    text = text.split(", ")
    if text[0] == "Mister":
        text[0] = "Mr."
    elif text[0] == "Miss":
        text[0] = "Ms."
    print("%s" %("*" * 20))
    print("Registration Confirm")
    print("%s" %("*" * 20))
    print("%s %s %s" % (text[0], text[1], text[2]))
    print("Age: %i" % (int(text[3])))
    print("Matthayom: %i" % (int(text[4])))
    print("%s School" % (text[5]))
    print("%s" %("*" * 20))
    print("Thank You!")

main()
