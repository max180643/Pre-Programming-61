"""Election Chance"""
def main():
    """Main Function"""
    fail_per = int(input()) / 100
    year = int(input())
    chance = (1 - (fail_per * (year - 2018))) * 100
    check = 0 < chance <= 100
    chance = chance * check
    print(int(chance), "%")

main()
