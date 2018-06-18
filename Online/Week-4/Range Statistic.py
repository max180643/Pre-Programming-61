"""Range Statistic"""
def main():
    """Main Function"""
    amount = int(input())
    # nmax = 0
    # nmin = 0
    for i in range(amount):
        number = int(input())
        if i == 0:
        # if nmax == 0 and nmin == 0:1
            nmax, nmin = number, number
            # nmax = number
            # nmin = number
        nmax = max(number, nmax)
        nmin = min(number, nmin)
        # print(nmax, nmin)
    print(nmax - nmin)

main()
