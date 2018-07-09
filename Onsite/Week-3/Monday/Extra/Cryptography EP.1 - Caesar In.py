"""Cryptography EP.1 - Caesar In"""
def main():
    """Main Function"""
    char = ord(input())
    if 65 <= char <= 90 or 97 <= char <= 122:
        if 97 <= char <= 99:
            char += 23
        elif 65 <= char <= 67:
            char += 23
        else:
            char -= 3
    print(chr(char))

main()
