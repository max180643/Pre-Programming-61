"""Dorm EP.1 - Speedtest"""
def main():
    """Main Function"""
    speed1 = float(input())
    speed2 = float(input())
    speed3 = float(input())
    speed4 = float(input())
    speed5 = float(input())
    speed6 = float(input())
    print("%.2f Mbps"%(max(speed1, speed2, speed3, speed4, speed5, speed6)))

main()
