"""How many characters?"""
def main():
    """Main Function"""
    text = input()
    temp = ""
    for char in text:
        if char.isalpha() == True:
            temp += char
    for i in range(1, 27):
        for j in range(len(temp)):
            if chr(i + 64) == temp[j]:
                print("%s: %i" % (chr(i + 64), temp.count(chr(i + 64))))
                break
    for i in range(1, 27):
        for j in range(len(temp)):
            if chr(i + 96) == temp[j]:
                print("%s: %i" % (chr(i + 96), temp.count(chr(i + 96))))
                break

main()
