"""Mysterious Number"""
def main():
    """Main Function"""
    puzzle = float(input())
    while True:
        guess = float(input())
        if guess > puzzle:
            print("Too Much!")
        elif guess < puzzle:
            print("More!")
        else:
            print("Yeah!")
            break

main()
