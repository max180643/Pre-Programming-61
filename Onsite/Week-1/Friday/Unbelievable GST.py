"""Unbelievable GST"""
def main():
    """Main Function"""
    price = int(input())
    fine = int(input())
    total = price + fine
    service = total * 0.09
    vat = (total + service) * 0.075
    final = total + service + vat
    print("Total: %.2f THB" % (total))
    print("Service: %.2f THB" % (service))
    print("VAT: %.2f THB" % (vat))
    print("Final Price: %.2f THB" % (final))

main()
