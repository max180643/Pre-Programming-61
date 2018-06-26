"""Donut Area"""
def main():
    """Main Function"""
    donut = int(input())
    hole = int(input())
    pie = 3.14
    area = ((pie * donut ** 2) - (pie * hole ** 2))
    print("Donut Area is %.2f!"%(area))

main()
