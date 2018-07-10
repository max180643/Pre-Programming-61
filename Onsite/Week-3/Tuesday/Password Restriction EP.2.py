"""Password Restriction EP.2"""
def main():
    """Main Function"""
    text = input()
    if text.isdigit() == True:
        print("You can use this Password")
    else:
        print("You can't use this Password")

main()
