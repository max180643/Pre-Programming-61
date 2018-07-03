"""Grade"""
def main():
    """Main Function"""
    score = int(input())
    if 0 <= score <= 49:
        print("0")
    elif 50 <= score <= 54:
        print("1")
    elif 55 <= score <= 59:
        print("1.5")
    elif 60 <= score <= 64:
        print("2")
    elif 65 <= score <= 69:
        print("2.5")
    elif 70 <= score <= 74:
        print("3")
    elif 75 <= score <= 79:
        print("3.5")
    elif 80 <= score <= 100:
        print("4")
    else:
        print("Invalid")

main()
