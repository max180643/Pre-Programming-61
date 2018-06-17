"""Arithmetic Sequence"""
def main():
    """Main Function"""
    frist = int(input())
    amout = int(input())
    diff = int(input())
    for _ in range(amout):
        print(frist, end=" ")
        frist += diff

main()
