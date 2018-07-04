"""Airport"""
def main(way, hour_in, minute_in, time):
    """Main Function"""
    if time == "pm" and hour_in != 12: # covert to 13-23 hr
        hour_in += 12
    total = (hour_in * 60) + minute_in + 1440
    if way == "A":
        total -= 160
    elif way == "B":
        total -= 140
    elif way == "C":
        total -= 115
    hour, minute = divmod(total, 60) # convert to hr,min
    hour = hour % 24
    if hour < 12:
        print("%02d:%02dam" % (hour, minute))
    elif hour > 12:
        hour -= 12
        print("%02d:%02dpm" % (hour, minute))
    else:
        print("%02d:%02dpm" % (hour, minute))

main(input(), int(input()), int(input()), input())
