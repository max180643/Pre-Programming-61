"""Leap Year"""
def main():
    """Main Function"""
    year = int(input())
    if year <= 0:
        print("This year does not exist.")
    elif (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0):
        print("%i is leap year."% (year))
    else:
        print("%i is not leap year."% (year))

main()
