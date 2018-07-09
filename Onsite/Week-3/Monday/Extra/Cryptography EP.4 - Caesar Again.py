"""Cryptography EP.4 - Caesar Again"""
def main():
    """Main Function"""
    text = input()
    temp = ""
    for i in range(len(text)):
        char = ord(text[i])
        if 65 <= char <= 90 or 97 <= char <= 122:
            if 97 <= char <= 99:
                char += 23
                temp += chr(char)
            elif 65 <= char <= 67:
                char += 23
                temp += chr(char)
            else:
                char -= 3
                temp += chr(char)
        else:
            temp += text[i]
    print(temp)

main()
