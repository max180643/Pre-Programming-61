"""The Camp EP.5"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(input().lower())
        if "addictive substances" in box:
            box.remove("addictive substances")
        elif "cigarettes" in box:
            box.remove("cigarettes")
        elif "weapons" in box:
            box.remove("weapons")
        elif "alcohol" in box:
            box.remove("alcohol")
        elif "illegal items" in box:
            box.remove("illegal items")
    print("\n".join(box))

main()
