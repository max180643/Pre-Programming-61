"""Palindrome"""
def main():
    """Main Funciton"""
    text = input()
    if text == text[::-1]:
        print("Yes")
    else:
        print("No")

main()
