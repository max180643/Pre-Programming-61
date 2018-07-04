"""Geometric Series"""
def main():
    """Main Function"""
    frist = float(input())
    amount = int(input())
    joint = float(input())
    summ = 0
    for i in range(amount):
        if i == 0:
            summ += frist
        else:
            frist *= joint
            summ += frist
    print("%.2f" % (summ))

main()
