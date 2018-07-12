"""Just Insert"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(input())
    insert = int(input())
    text = input()
    box.insert(insert, text)
    print(box)

main()
