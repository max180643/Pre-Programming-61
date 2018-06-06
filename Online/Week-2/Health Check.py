"""Health Check"""
def main():
    """Main Function"""
    in1 = float(input())
    in2 = float(input())
    in3 = float(input())
    in4 = float(input())
    in5 = float(input())
    set1 = (in1, in2, in3, in4, in5)
    print("The Tallest is %.1f"%(max(set1)))
    print("The Shortest is %.1f"%(min(set1)))
    print("Average is %.1f"%(sum(set1) / len(set1)))

main()
