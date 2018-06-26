"""Shabu"""
def main():
    """Main Function"""
    price = float(input())
    print("Price\t%.2f THB"%(price))
    print("Service\t%.2f THB" % (price * 0.1))
    print("VAT\t%.2f THB" % ((price + price * 0.1) * 0.08))
    print("Total\t%.2f THB" % (price + (price * 0.1) + (price + price * 0.1) * 0.08))

main()
