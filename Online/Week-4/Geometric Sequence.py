"""Geometric Sequence"""
def main():
    """Main Function"""
    frist = float(input())
    amount = int(input())
    joint = float(input())
    for _ in range(amount):
        print("%.2f"%(frist), end=" ")
        frist *= joint

main()
