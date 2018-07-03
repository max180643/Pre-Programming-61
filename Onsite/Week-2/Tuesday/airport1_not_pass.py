"""Airport"""
def main():
    """Main Function"""
    # input
    way = input()
    hour_in = int(input())
    minute_in = int(input())
    total = hour_in * 60 + minute_in - 45
    type_time = input()
    # check way
    if way == "A":
        total = total - 115
    elif way == "B":
        total = total - 95
    elif way == "C":
        total = total - 70
    hour, minute = divmod(total, 60)
    #print(hour, minute)
    # check type
    if hour < 0 and type_time == "am":
        hour = hour + 12
        type_time = "pm"
        #print("if1")
    elif hour < 0 and type_time == "pm":
        hour = hour + 12
        type_time = "am"
        #print("if2")
    elif hour == 0 and minute == 0 and type_time == "am": # 2:40am - 2hr:40m
        hour = hour + 12
        type_time = "pm"
        #print("if3")
    elif hour == 0 and minute == 0 and type_time == "pm":
        hour = hour + 12
        type_time = "am"
        #print("if4")
    elif hour == 0 and type_time == "am":
        hour = hour + 12
        #print("if5")
    elif hour == 0 and type_time == "pm":
        hour = hour + 12
        #print("if6")
    elif (hour_in * 60 + minute_in) > 720 and type_time == "am": # 12:30 - 2hr:40m
        type_time = "pm"
        #print("if7")
    elif (hour_in * 60 + minute_in) > 720 and type_time == "pm":
        type_time = "am"
        #print("if8")

    print("%02i:%02i%s" % (hour, minute, type_time))

main()
