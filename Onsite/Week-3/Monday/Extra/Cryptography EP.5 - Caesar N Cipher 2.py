"""Cryptography EP.5 - Caesar N Cipher 2"""
def main():
    """Main Function"""
    num = int(input()) % 26
    text = input()
    temp = ""
    for i in range(len(text)):
        char = ord(text[i])
        if 65 <= char <= 90 or 97 <= char <= 122:
            if 97 <= char <= (97 + num - 1):
                char += 25 - num + 1
                temp += chr(char)
            elif 65 <= char <= (65 + num - 1):
                char += 25 - num + 1
                temp += chr(char)
            else:
                char -= num
                temp += chr(char)
        else:
            temp += text[i]
    print(temp)

main()
