"""Skipping"""
def main():
    """Main Function"""
    number = int(input())
    come = int(input())
    for i in range(1, number + 1, come):
        print(i)

main()
