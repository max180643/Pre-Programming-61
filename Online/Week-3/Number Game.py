"""Number Game"""
def main():
    """Main Function"""
    coke = int(input())
    saint1 = int(input())
    gun1 = int(input())
    saint2 = int(input())
    gun2 = int(input())
    saint3 = int(input())
    gun3 = int(input())
    saint = abs(coke - (saint1 + saint2 + saint3))
    gun = abs(coke - (gun1 + gun2 + gun3))
    if saint < gun:
        print("Saint won!")
    if gun < saint:
        print("Gunn won!")
    if saint == gun:
        print("Draw!")

main()
