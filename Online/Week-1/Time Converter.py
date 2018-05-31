"""Time Converter"""

def main():
    """Main Function"""
    second = int(input())
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    print("%d Hour(s) %d Minute(s) %d Second(s)" % (hour, minute, second))

main()
