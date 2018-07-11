"""ThreeSUM"""
def main():
    """Main Function"""
    num = int(input())
    player1 = input()
    player2 = input()
    player3 = input()
    num_total = 0
    for i in range(1, num + 1):
        num_total += i
    winner = num_total % 3
    if winner == 0:
        print("Winner is %s!!" % (player3))
    elif winner == 1:
        print("Winner is %s!!" % (player1))
    elif winner == 2:
        print("Winner is %s!!" % (player2))

main()
