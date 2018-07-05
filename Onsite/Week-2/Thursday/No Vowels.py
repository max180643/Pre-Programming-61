"""No Vowels"""
def main():
    """Main Function"""
    text = input()
    vowel = "AEIOUaeiou"
    for i in vowel:
        text = text.replace(i, "")
    print(text)

main()
