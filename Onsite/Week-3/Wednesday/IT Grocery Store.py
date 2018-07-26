"""IT Grocery Store"""
def main():
    """Main Function"""
    money = 1000
    amount = int(input())
    price = int(input())
    if price <= 0 or amount <= 0:
        print("1000")
    else:
        # total check
        if amount > 15:
            price -= price % 10
        elif 10 < amount <= 15:
            price -= 5
        # price check
        if price <= 150:
            price -= 1
        elif 150 < price <= 300:
            price -= 10
        elif price > 300:
            price -= 20
        # output
        if money - price >= 0:
            print(money - price)
        else:
            print("Not enough money")

main()
