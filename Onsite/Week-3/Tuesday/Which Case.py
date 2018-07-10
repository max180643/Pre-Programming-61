"""Which Case?"""
def main():
    """Main Function"""
    text = input()
    if text.isupper() == True:
        print("This sentence is written in uppercase.")
    elif text.islower() == True:
        print("This sentence is written in lowercase.")
    else:
        print("This sentence is written in both uppercase and lowercase.")

main()
