"""Backward Skipping"""
def main():
    """Main Function"""
    number = int(input())
    talk = int(input())
    for i in range(number, -1, -talk):
        print(i)

main()
