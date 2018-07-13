"""Median"""
def main():
    """Main Function"""
    text = input()
    text = text.split(", ")
    size = len(text)
    for i in range(len(text)):
        text[i] = float(text[i])
    text.sort()
    if size % 2 == 1:
        print("%.2f" % (float(text[size // 2])))
    else:
        print("%.2f" % (float(((text[size // 2 - 1]) + (text[size // 2])) / 2)))

main()
