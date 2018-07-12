"""Replace It"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(input())
    replace = int(input())
    box[replace] = input()
    print(box)

main()
