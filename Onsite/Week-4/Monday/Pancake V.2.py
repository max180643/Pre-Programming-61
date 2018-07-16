"""Pancake V.2"""
def main():
    """Main Function"""
    promo_buy = int(input()) # ซื้อถึงแล้วได้แถม
    promo_give = int(input()) # จำนวนแถม
    want = int(input()) # ต้องการ
    price = int(input()) # ราคาต่อชิ้น
    pack = promo_buy + promo_give #จำนวนชิ้นในแพ็ค
    buypack = want // pack #จำนวนแพ็คที่ต้องซื้อ
    other = want - (buypack * pack) # เศษที่เหลือจากการซื้อแพค
    if other >= promo_buy: # ถ้าเศษมากกว่าหรือเท่ากับ จำนวนโปรโมชั่น
        buypack += 1
        other = 0
    get = (pack * buypack) + other
    pay = ((promo_buy * buypack) + other) * price
    # Output
    print("Pay: %i" % (pay))
    print("Get: %i" % (get))

main()
