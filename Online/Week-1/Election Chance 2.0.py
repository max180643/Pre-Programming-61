"""Election Chance"""
def main():
    """Main Function"""
    fail_per = int(input()) / 100
    year = int(input())
    chance = (1 - (fail_per * (year - 2018))) * 100
    print(int(chance * (0 < chance <= 100)), "%")

main()
