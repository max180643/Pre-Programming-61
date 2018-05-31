""""Bank Notes"""
def main():
    """Main Function"""
    total = int(input())
    total, total1 = divmod(total, 1000)
    total1, total2 = divmod(total1, 500)
    total2, total3 = divmod(total2, 100)
    total3, total4 = divmod(total3, 50)
    total4, total5 = divmod(total4, 20)
    total5 = total5 // 10
    print(total)
    print(total1)
    print(total2)
    print(total3)
    print(total4)
    print(total5)

main()
