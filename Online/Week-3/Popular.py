"""Popular"""
def main():
    """Main Function"""
    know = 0
    if "Yes" in input():
        know = know + 1
    if "Yes" in input():
        know = know + 1
    if "Yes" in input():
        know = know + 1
    if "Yes" in input():
        know = know + 1
    if "Yes" in input():
        know = know + 1
    if know == 5:
        print("Superstar")
    elif know == 4:
        print("Very Popular")
    elif know == 3:
        print("Popular")
    elif know == 2 or know == 1:
        print("Ordinary Student")
    else:
        print("Invisible")

main()
