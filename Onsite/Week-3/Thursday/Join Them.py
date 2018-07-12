"""Join Them"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(input())
    key = input()
    print(key.join(box))

main()
