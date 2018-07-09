"""First and Last"""
def main():
    """Main Function"""
    text = input()
    if text[0] == text[len(text) - 1]:
        print("Yes")
    else:
        print("No")

main()
