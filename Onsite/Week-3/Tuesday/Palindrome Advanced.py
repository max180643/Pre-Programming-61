"""Palindrome Advanced"""
def main():
    """Main Function"""
    text = input().lower()
    text = text.replace(" ", "")
    text2 = text[::-1]
    if text == text2:
        print("Yes")
    else:
        print("No")

main()
