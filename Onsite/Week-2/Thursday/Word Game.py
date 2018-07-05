"""Word Game"""
def main():
    """Main Function"""
    score = 100
    key = input()
    while True:
        ans = input()
        if ans == key:
            print("Correct!! You've %i points remaining." % (score))
            break
        elif ans != key:
            score -= 5
        if score == 0:
            print("Game Over!")
            break

main()
