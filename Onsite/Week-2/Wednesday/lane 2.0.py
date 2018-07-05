"""Lane"""
def main():
    """Main Function"""
    lane = 1
    while True:
        lane_in = input()
        if lane_in == "L" and lane != 1:
            lane -= 1
        elif lane_in == "R" and lane != 4:
            lane += 1
        elif lane_in == "P":
            break
    print(lane)

main()
