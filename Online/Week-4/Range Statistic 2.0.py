"""Range Statistic"""
def main():
    """Main Function"""
    amount = int(input())
    for i in range(amount):
        number = int(input())
        if i == 0:
            nmax, nmin = number, number
        nmax = max(number, nmax)
        nmin = min(number, nmin)
    print(nmax - nmin)

main()
