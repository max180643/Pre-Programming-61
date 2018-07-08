"""Cake"""
import math as m
def main():
    """"Main Function"""
    global top1, bottom1, top2, bottom2, temp, gcd1, gcd2
    num = int(input())
    top1 = int(input())
    bottom1 = int(input())
    temp = 0
    gcd1 = 0
    gcd2 = 0
    for _ in range(num - 1):
        top2 = int(input())
        bottom2 = int(input())
        # check
        temp = min(bottom1, bottom2)
        for i in range(2, temp + 1):
            if bottom1 % i == 0 and bottom2 % i == 0:
                gcd1 = bottom1 // i
                gcd2 = bottom2 // i
                bottom1 *= gcd2
                top1 *= gcd2
                bottom2 *= gcd1
                top2 *= gcd1
                break
        else:
            temp = bottom1
            top1 *= bottom2
            bottom1 *= bottom2
            top2 *= temp
            bottom2 *= temp
        #
        bottom1 = bottom2
        top1 += top2
    # output
    print(m.ceil(top1 / bottom2))
    if top1 % bottom1 == 0:
        print("0")
    else:
        print("%i/%i" % (bottom1 - (top1 % bottom2), bottom1))

main()
