"""Number List"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(int(input()))
    box.sort()
    print(box)

main()
