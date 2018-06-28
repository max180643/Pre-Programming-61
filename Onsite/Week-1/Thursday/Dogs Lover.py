"""Dogs Lover"""
def main():
    """Main function"""
    mon1 = sale(int(input()), int(input()))
    mon2 = sale(int(input()), int(input()))
    mon3 = sale(int(input()), int(input()))
    mon4 = sale(int(input()), int(input()))
    print("%.2f" % (mon1 + mon2 + mon3 + mon4))

def sale(price1, price2):
    """Sale Promotion"""
    ans = (price1 + price2) * 0.85
    return ans

main()
