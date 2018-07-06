"""Digital Clock"""
def main():
    """Main Function"""
    type_time = ""
    # Check Time
    hour = int(input())
    if hour >= 24 or hour < 0:
        print("Invalid Time")
    else:
        minute = int(input())
        if minute < 0 or minute >= 60:
            print("Invalid Time")
        else:
            # Check1 24hr to 12hr
            if hour >= 0 and hour <= 11:
                type_time = "AM"
            elif hour >= 12 and hour <= 23:
                type_time = "PM"
                hour -= 12
                if hour == 0 and type_time == "PM":
                    hour = 12
            # Output
            print("%i:%02i %s" % (hour, minute, type_time))

main()
