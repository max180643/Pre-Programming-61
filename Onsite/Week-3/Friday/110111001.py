"""110111001"""
def main():
    """Main Fuction"""
    text = input()
    temp = ""
    for i in text:
        if i == "0" or i == "1":
            temp += i
    print(temp)

main()
