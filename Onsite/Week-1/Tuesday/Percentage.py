"""Percentage"""
def main():
    """Main Function"""
    total = int(input())
    limit = int(input())
    item = input()
    percent = total / limit * 100
    print("%s %.2f%%"%(item, percent))

main()
