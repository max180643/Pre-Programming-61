"""Speed"""
def main():
    """Main Function"""
    distant = int(input()) / 1000
    time = int(input()) / 60 / 60
    speed = distant / time
    print("%.2f"%(speed))

main()
