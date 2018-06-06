"""Black Canyon"""
def main():
    """Main Function"""
    set1 = promotion(int(input()), int(input()))
    set2 = promotion(int(input()), int(input()))
    set3 = promotion(int(input()), int(input()))
    set4 = promotion(int(input()), int(input()))
    set5 = promotion(int(input()), int(input()))
    price = set1 + set2 + set3 + set4 + set5
    total = price - (price * 0.10)
    print("Total : %.2f Baht"%(total))

def promotion(drink, cake):
    """Promotiom"""
    total = (drink + cake) - ((drink + cake) * 0.20)
    return total

main()
