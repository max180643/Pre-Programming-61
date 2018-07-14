"""Summer Sale"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        text = input().split(" = ")
        box.append(text)
    box.sort(key=min)
    print("%s is only $%.2f!" % (box[0][0], float(box[0][1])))

main()
