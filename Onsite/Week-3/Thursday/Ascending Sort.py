"""Ascending Sort"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(int(input()))
    box.sort()
    for i in range(num):
        print(box[i])

main()
