"""FourSUM"""
def main():
    """Main Function"""
    num = int(input())
    player1 = input()
    player2 = input()
    player3 = input()
    player4 = input()
    num_total = (num / 2) * (num + 1)
    if num_total % 4 == 0:
        print("Winner is %s!!" % (player4))
    elif num_total % 4 == 1:
        print("Winner is %s!!" % (player1))
    elif num_total % 4 == 2:
        print("Winner is %s!!" % (player2))
    elif num_total % 4 == 3:
        print("Winner is %s!!" % (player3))

main()
