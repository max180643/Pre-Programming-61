"""Sleepy"""
def main():
    """Main Function"""
    day1 = time(int(input()), int(input()), int(input()))
    day2 = time(int(input()), int(input()), int(input()))
    day3 = time(int(input()), int(input()), int(input()))
    day4 = time(int(input()), int(input()), int(input()))
    day5 = time(int(input()), int(input()), int(input()))
    day6 = time(int(input()), int(input()), int(input()))
    day7 = time(int(input()), int(input()), int(input()))
    day8 = time(int(input()), int(input()), int(input()))
    day9 = time(int(input()), int(input()), int(input()))
    day10 = time(int(input()), int(input()), int(input()))
    print("[Day 01] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day1))
    print("[Day 02] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day2))
    print("[Day 03] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day3))
    print("[Day 04] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day4))
    print("[Day 05] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day5))
    print("[Day 06] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day6))
    print("[Day 07] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day7))
    print("[Day 08] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day8))
    print("[Day 09] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day9))
    print("[Day 10] %02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))" % (day10))

def time(hour_, minute_, lazy):
    """Time"""
    hour_c = hour_ * 60 #convert to minute
    getup = (hour_c + minute_) + (10 + (lazy * 1)) + (40 + (lazy * 5)) + 15
    hour, minute = divmod(getup, 60)
    used = getup - (hour_c + minute_)
    hour_u, minute_u = divmod(used, 60)
    return hour_, minute_, hour, minute, hour_u, minute_u

main()
