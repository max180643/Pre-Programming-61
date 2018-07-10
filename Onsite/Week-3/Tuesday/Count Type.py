"""Count Type"""
def main():
    """Main Function"""
    text = input()
    upper = 0
    lower = 0
    num = 0
    other = 0
    for i in text:
        if i.isupper() == True:
            upper += 1
        elif i.islower() == True:
            lower += 1
        elif i.isdigit() == True:
            num += 1
        else:
            other += 1
    print("Uppercase : %i" % (upper))
    print("Lowercase : %i" % (lower))
    print("Numeric : %i" % (num))
    print("Other : %i" % (other))

main()
