"""Leaderboard Average"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    total = 0
    if num > 0:
        for i in range(num):
            box.append(input().split(", "))
        for i in range(num):
            total += float(box[i][2])
        print("%.2f" % (total / num))

main()
