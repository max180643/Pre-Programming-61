"""Cryptography EP.3 - Caesar N Cipher"""
def main():
    """Main Function"""
    num = int(input()) % 26
    char = ord(input())
    if 65 <= char <= 90 or 97 <= char <= 122:
        if 97 <= char <= (97 + num - 1):
            char += 25 - num + 1
        elif 65 <= char <= (65 + num - 1):
            char += 25 - num + 1
        else:
            char -= num
    print(chr(char))

main()
