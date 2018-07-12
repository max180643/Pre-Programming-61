"""The Camp EP.5"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    illegal = ["addictive substances", "cigarettes", "weapons", "alcohol", "illegal items"]
    for _ in range(num):
        box.append(input().lower())
    for i in range(num):
        if box[i] not in illegal:
            print(box[i])

main()
