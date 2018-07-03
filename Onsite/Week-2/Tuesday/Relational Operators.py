"""Relational Operators"""
def main():
    """Main Function"""
    num1 = int(input())
    num2 = int(input())
    if num2 == num1:
        print("Correct!")
    elif num2 > num1:
        print("Too High")
    elif num2 < num1:
        print("Too Low")

main()
