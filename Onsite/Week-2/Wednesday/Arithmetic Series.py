"""Arithmetic Series"""
def main():
    """Main Function"""
    first = int(input())
    amount = int(input())
    diff = int(input())
    summ = 0
    for i in range(amount):
        if i == 0:
            summ += first
        else:
            first = first + diff
            summ += first
    print(summ)

main()
