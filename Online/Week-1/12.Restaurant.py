""""Restaurant"""
def main():
    """Main Function"""
    price = int(input())
    vat = price * 0.07
    service_charge = price * 0.10
    price_total = (price + vat + service_charge)
    print("Service Charge : %.2f Baht"%service_charge)
    print("VAT : %.2f Baht"%vat)
    print("Total : %.2f Baht"%price_total)

main()
