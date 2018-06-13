"""Bedtime"""
def main():
    """Main Function"""
    # input
    hour_s = int(input())
    min_s = int(input())
    hour_w = int(input())
    min_w = int(input())
    # hour
    if hour_s > hour_w:
        hour = 24 - hour_s + hour_w
    else:
        hour = hour_w - hour_s
    # minute
    if min_s > min_w:
        if hour_s == hour_w:
            hour = 23
            minute = 60 - min_s + min_w
        else:
            hour = hour - 1
            minute = 60 - min_s + min_w
    else:
        minute = min_w - min_s
    # 24 hour
    if hour == 0 and minute == 0:
        hour = 24
    # check
    if hour >= 10:
        print("Too much")
    elif hour >= 7:
        print("Enough")
    elif hour < 7:
        print("Not enough")
    # print(hour,minute)

main()
