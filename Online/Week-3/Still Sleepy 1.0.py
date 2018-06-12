"""Still Sleepy"""
def main():
    """Main Function"""
    hour = int(input())
    minute = int(input())
    time = hour * 60 + minute
    prepare = 10 + 40 + 15
    # check
    if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
        if time >= 540:  # 9:00
            output = "Continued sleeping"
        elif time >= 495:  # 8:15
            used = prepare - 10 - 6 - 9 - 8
            output = time + used
        elif time >= 480:  # 8:00
            used = prepare - 10 - 6 - 9
            output = time + used
        elif time >= 465:  # 7:45
            used = prepare - 10 - 6
            output = time + used
        elif time >= 450:  # 7:30
            used = prepare - 10
            output = time + used
        else:
            used = prepare
            output = time + prepare
        # output
        if hour < 9:
            # time
            hour1, min1 = divmod(output, 60)
            hour_u, min_u = divmod(used, 60)
            print("%02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s)" % (
            hour, minute, hour1, min1, hour_u, min_u))
        else:
            print(output)

main()
