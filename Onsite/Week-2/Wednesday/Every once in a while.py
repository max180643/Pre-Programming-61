"""Every once in a while"""
def main():
    """Main Function"""
    number1 = int(input())
    number2 = int(input())
    if number1 > 0:
        for i in range(1, number1 + 1, number2):
            print(i)
    else:
        for i in range(-1, number1 - 1, -number2):
            print(i)

main()
