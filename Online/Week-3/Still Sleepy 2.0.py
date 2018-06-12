"""Still Sleepy"""
def main():
    """Main Function"""
    hour = int(input())
    minute = int(input())
    time = hour * 60 + minute
    prepare = 10 + 40 + 15
    if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
        if hour >= 9:
            print("Continued sleeping")
        elif hour >= 8 and minute >= 15:
            used = prepare - 10 - 6 - 9 - 8
            use(hour, minute, time + used, used)
        elif hour >= 8:
            used = prepare - 10 - 6 - 9
            use(hour, minute, time + used, used)
        elif hour >= 7 and minute >= 45:
            used = prepare - 10 - 6
            use(hour, minute, time + used, used)
        elif hour >= 7 and minute >= 30:
            used = prepare - 10
            use(hour, minute, time + used, used)
        else:
            used = prepare
            use(hour, minute, time + used, used)

def use(hour, minute, output, used):
    """Output"""
    hour1, min1 = divmod(output, 60)
    hour_u, min_u = divmod(used, 60)
    print("%02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (
        hour, minute, hour1, min1, hour_u, min_u))

main()
