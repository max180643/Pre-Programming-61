"""Change"""
def main():
    """Main Function"""
    amount = int(input())
    price = int(input())
    change = amount - price
    change, change1 = divmod(change, 100)
    change1, change2 = divmod(change1, 50)
    change2, change3 = divmod(change2, 20)
    change3, change4 = divmod(change3, 10)
    change4, change5 = divmod(change4, 5)
    change5, change6 = divmod(change5, 2)
    change6 = change6 // 1
    print("%i\n%i\n%i\n%i\n%i\n%i\n%i"%\
          (change, change1, change2, change3, change4, change5, change6))

main()
