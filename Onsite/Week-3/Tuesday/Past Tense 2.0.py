"""Past Tense"""
def main():
    """Main Function"""
    text = input()
    text = text.replace(" is", " was")
    text = text.replace(" are", " were")
    text = text.replace("Is", "Was")
    text = text.replace("Are", "Were")
    print(text)

main()
