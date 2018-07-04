"""Kangaroo"""
def main():
    """Main Function"""
    varx1 = int(input())
    varv1 = int(input())
    varx2 = int(input())
    varv2 = int(input())
    if varv1 < varv2 or varx1 > varx2 or varv1 == varv2:
        print("NO")
    elif varx2 > varx1 >= 0:
        while True:
            varx1 += varv1
            varx2 += varv2
            if varx1 > varx2:
                print("NO")
                break
            elif varx1 == varx2:
                print("YES")
                break

main()
