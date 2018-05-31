"""Pizza Delivery"""
def main():
    """Main Function"""
    distance = float(input())
    speed = int(input())
    dis_convert = (distance * 1000)
    second = (dis_convert / speed)
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    print("%d Hour(s) %d Minute(s) %d Second(s)" % (hour, minute, second))

main()
