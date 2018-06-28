"""Broken Watch"""
def main():
    """Main Function"""
    set1 = convert(int(input()))
    set2 = convert(int(input()))
    set3 = convert(int(input()))
    print("%s\n%s\n%s" % (set1, set2, set3))

def convert(second):
    """Convert Time"""
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    return "%i Hour(s) %i Minute(s) %i Second(s)" % (hour, minute, second)

main()
