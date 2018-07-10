"""Grade A"""
def main():
    """Main Function"""
    text = input().upper()
    text = text.count("A")
    if text > 0:
        print(text)
    else:
        print("Oops")

main()
