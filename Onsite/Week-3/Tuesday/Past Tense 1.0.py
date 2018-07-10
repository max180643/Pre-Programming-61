"""Past Tense"""
def main():
    """Main Function"""
    text = input()
    text = text.split(" ")
    total = len(text)
    temp = ""
    for i in range(total):
        if text[i] == "is":
            text[i] = "was"
            temp += (text[i] + " ")
        elif text[i] == "Is":
            text[i] = "Was"
            temp += (text[i] + " ")
        elif text[i] == "are":
            text[i] = "were"
            temp += (text[i] + " ")
        elif text[i] == "Are":
            text[i] = "Were"
            temp += (text[i] + " ")
        else:
            temp += (text[i] + " ")
    print(temp)

main()
