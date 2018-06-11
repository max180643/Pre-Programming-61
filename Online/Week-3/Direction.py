"""Direction"""
def main():
    """Main Function"""
    pos_x = int(input())
    pos_y = int(input())
    if pos_x == 0 and pos_y == 0:
        print("Origin")
    if pos_x == 0 and pos_y > 0:
        print("North")
    if pos_x == 0 and pos_y < 0:
        print("South")
    if pos_x > 0 and pos_y == 0:
        print("East")
    if pos_x < 0 and pos_y == 0:
        print("West")
    if pos_x > 0 and pos_y > 0:
        print("Northeast")
    if pos_x < 0 and pos_y > 0:
        print("Northwest")
    if pos_x > 0 and pos_y < 0:
        print("Southeast")
    if pos_x < 0 and pos_y < 0:
        print("Southwest")

main()
