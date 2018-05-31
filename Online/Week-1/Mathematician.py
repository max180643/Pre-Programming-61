"""Mathematician"""
def main():
    """Main Function"""
    line = float(input())
    pie = 3.141
    circle_line = (2 * pie * line)
    circle_area = (pie * (line ** 2))
    print("C = %.3f"%circle_line)
    print("A = %.3f"%circle_area)

main()
