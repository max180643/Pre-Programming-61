"""Energy"""
def main():
    """Main Function"""
    distance = float(input())
    energy = int(input())
    dis_to_meter = distance * 1000
    energy_to_meter = energy * 10
    stick = (dis_to_meter / energy_to_meter)
    print(int(stick) + (stick - (int(stick)) != 0))

main()
