"""Classroom"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        temp = []
        name = input()
        score = int(input())
        temp.append(score)
        temp.append(name)
        box.append(temp)
    box.sort()
    for i in box:
        print(*i)

main()
