"""Kangaroo"""
def main(loc1, dist1, loc2, dist2):
    """Main Function"""
    if dist1 <= dist2 or loc1 > loc2:
        print("NO")
    elif 0 <= loc1 < loc2:
        while True:
            loc1 += dist1
            loc2 += dist2
            if loc1 == loc2:
                print("YES")
                break
            elif loc1 > loc2:
                print("NO")
                break

main(int(input()), int(input()), int(input()), int(input()))
