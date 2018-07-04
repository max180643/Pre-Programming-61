"""Airport"""
def main():
    """Main Function"""
    # input
    way = input()
    hour_in = int(input())
    minute_in = int(input())
    total = hour_in * 60 + minute_in
    type_time = input()
    # check way
    if way == "A":
        total = total - 160
    elif way == "B":
        total = total - 140
    elif way == "C":
        total = total - 115
    hour, minute = divmod(total, 60)
    # check type
    if hour < 0 and type_time == "am":
        hour = hour + 12
        type_time = "pm"
    elif hour < 0 and type_time == "pm":
        hour = hour + 12
        type_time = "am"
    elif hour == 0 and minute == 0 and type_time == "pm":
        hour = hour + 12
    elif hour == 0 and type_time == "pm":
        hour = hour + 12
    elif (hour_in * 60 + minute_in) >= 720 and type_time == "pm":
        type_time = "am"

    print("%02i:%02i%s" % (hour, minute, type_time))

main()
