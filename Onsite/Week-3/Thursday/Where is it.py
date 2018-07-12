"""Where is it"""
def main():
    """Main Function"""
    num = int(input())
    box = []
    for _ in range(num):
        box.append(int(input()))
    find = int(input())
    print("%i is at index %i" % (find, box.index(find)))

main()
