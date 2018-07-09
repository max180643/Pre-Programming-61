"""Cake"""
def main():
    """Main Function"""
    top1, bottom1 = 0, 1
    num = int(input())
    for i in range(num):
        top2 = int(input())
        bottom2 = int(input())
        if bottom2 == bottom1: #ส่วนเท่ากัน
            top1 = top1 + top2
        else: #ส่วนไม่เท่ากัน
            left = top1 * bottom2
            right = bottom1 * top2
            suan = bottom1 * bottom2
            top1 = left + right
            bottom1 = suan
    need = top1 // bottom1 + (top1 % bottom1 != 0) #ต้องซื้อ
    print(need)
    if need == top1 // bottom1: #พอดี ไม่เหลือ
        print("0")
    else: #เหลือกิน
        var_x, var_y = need, 1
        left = var_x * bottom1
        right = var_y * top1
        top1 = left - right
        bottom1 = var_y * bottom1
        # หาเศษส่วนอย่างต่ำ
        temp = 1
        for i in range(1, bottom1 + 1):
            if top1 % i == 0 and bottom1 % i == 0:
                temp = i
        print("%d/%d" % (top1 // temp, bottom1 // temp))

main()
