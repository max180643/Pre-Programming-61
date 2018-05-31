"""Any Tax"""
def main():
    """Main Function"""
    price = int(input())
    price_service = price + (price * 0.10)
    price_vat = price_service + (price_service * 0.07)
    print(int(price_vat))

main()
