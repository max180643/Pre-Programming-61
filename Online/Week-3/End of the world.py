""""End of the world"""
def main():
    """Main Function"""
    # input
    msg = input()
    power = int(input())
    defense = int(input())
    # condition
    if defense > power * 30 / 100:
        power = power - (power * 45 / 100)
    if msg == "Justify yourself!":
        power = power - (power * 20 / 100)
    # check
    total = power - defense
    if total <= 0:
        print("We saved the world!")
    elif total > 1000:
        print("End of the world.")
    else:
        print("A great loss.")

main()
