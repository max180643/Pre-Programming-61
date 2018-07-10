"""Password Restriction EP.1"""
def main():
    """Main Function"""
    text = input()
    if text.isalpha() == True:
        print("You can use this Password")
    else:
        print("You can't use this Password")

main()
