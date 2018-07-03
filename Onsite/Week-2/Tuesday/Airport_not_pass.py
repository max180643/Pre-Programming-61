"""Airport"""
def main():
    """Main Function"""
    # input
    way = input()
    hour = int(input()) * 60
    minute = int(input())
    total = hour + minute - 45
    type_time = input()
    # check way
    if way == "A":
        total = total - 115
    elif way == "B":
        total = total - 95
    elif way == "C":
        total = total - 70
    hour, minute = divmod(total, 60)
    # check type
    if hour < 0 and type_time == "am": # am to pm ย้อน
        hour = hour + 12
        type_time = "pm"
    elif hour > 12 and type_time == "am": # am to pm ตาม
        hour = hour - 12
        type_time = "pm"
    elif hour < 0 and type_time == "pm": # pm to am ย้อน
        hour = hour + 12
        type_time = "am"
    elif hour > 12 and type_time == "pm": # pm to am ตาม
        hour = hour - 12
        type_time = "am"
    elif hour == 10 and type_time == "pm":
        type_time = "am"
    elif hour == 10 and type_time == "am":
        type_time = "pm"
    elif hour == 0 and type_time == "pm":
        hour = 12


    print("%02i:%02i%s" % (hour, minute, type_time))


main()
