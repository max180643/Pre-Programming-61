"""FirstROR"""
def main():
    """Main Function"""
    text = input()
    if "first" in text and "ror" in text and "mak" in text:
        print("P'First ror mak mak!!")
    elif ("ror" in text and "mak" in text) or ("first" in text and "mak" in text):
        print("I think so!!")
    elif "first" in text and "ror" in text:
        print("I'm so First!!")
    else:
        print("First == ror -> is always True!!")

main()
