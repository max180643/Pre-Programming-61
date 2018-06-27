"""Middle Value"""
def main():
    """Main Function"""
    price1 = int(input())
    price2 = int(input())
    price3 = int(input())
    middle = ((price1 + price2 + price3) \
              - max(price1, price2, price3) - min(price1, price2, price3))
    print(middle)

main()
