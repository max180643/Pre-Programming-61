"""Empty Fridge"""
def main():
    """Main Function"""
    check1 = int(input())
    check2 = int(input())
    check3 = int(input())
    check4 = int(input())
    check5 = int(input())
    print("-Shopping List-")
    check("Cola", 12, check1)
    check("Tea", 16, check2)
    check("Orange Juice", 20, check3)
    check("Strawberry Juice", 24, check4)
    check("Milk", 32, check5)

def check(item, require, remain):
    """Check Function"""
    if remain < require:
        print("%s x%i"% (item, require - remain))

main()
