"""Month Days Advanced"""
def main():
    """Main Function"""
    month = int(input())
    year = int(input())
    if year > 0 and 0 < month < 13:
        if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0) and month == 2:
            print("29")
        elif month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
            print("31")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30")
        elif month == 2:
            print("28")
    else:
        print("Invalid Month or Year")

main()
