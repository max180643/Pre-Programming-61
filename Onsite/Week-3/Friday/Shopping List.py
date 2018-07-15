"""Shopping List"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    count = 0
    for _ in range(num):
        text = input().split(", ")
        count += len(text)
        box.append(text)
    print("Total: %i" % (count - num))
    for i in range(num):
        print("%i at %s %s" % (len(box[i]) - 1, box[i].pop(0), box[i]))

main()
