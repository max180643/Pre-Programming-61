"""Match Winner"""
def main():
    """Main Function"""
    set1 = check(1)
    set2 = check(2)
    set3 = check(3)
    set4 = check(4)
    set5 = check(5)
    set6 = check(6)
    print("%s\n%s\n%s\n%s\n%s\n%s" % (set1, set2, set3, set4, set5, set6))

def check(match):
    """Check Score"""
    team1 = input()
    score1 = int(input())
    team2 = input()
    score2 = int(input())
    if score1 > score2:
        return "Match #%i: %s" % (match, team1)
    elif score2 > score1:
        return "Match #%i: %s" % (match, team2)
    else:
        return "Match #%i: %s" % (match, "Tie!")

main()
