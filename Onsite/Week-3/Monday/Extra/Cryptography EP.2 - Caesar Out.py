"""Cryptography EP.2 - Caesar Out"""
def main():
    """Main Function"""
    char = ord(input())
    if 65 <= char <= 90 or 97 <= char <= 122:
        if 88 <= char <= 90:
            char -= 23
        elif 120 <= char <= 122:
            char -= 23
        else:
            char += 3
    print(chr(char))

main()
