""""Admission"""
def main():
    """Main Function"""
    # input
    input_score = int(input())
    set1 = input()
    set2 = input()
    set3 = input()
    set4 = input()
    if input_score >= check(set1):
        print(set1)
    elif input_score >= check(set2):
        print(set2)
    elif input_score >= check(set3):
        print(set3)
    elif input_score >= check(set4):
        print(set4)
    else:
        print("None")

def check(set_in):
    """Check Function"""
    score = 0
    if set_in == "A":
        score += 20000
    if set_in == "B":
        score += 17500
    if set_in == "C":
        score += 18000
    if set_in == "D":
        score += 28250
    if set_in == "E":
        score += 27000
    if set_in == "F":
        score += 25000
    if set_in == "G":
        score += 21750
    if set_in == "H":
        score += 22000
    return score

main()
