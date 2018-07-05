"""Lane"""
def main():
    """Main Function"""
    lane = 1
    lane_in = ""
    while True:
        lane_in = input()
        if lane_in == "L":
            lane -= 1
        elif lane_in == "R":
            lane += 1
        elif lane_in == "P":
            break
        if lane < 1:
            lane = 1
        elif lane > 4:
            lane = 4
    print(lane)

main()
