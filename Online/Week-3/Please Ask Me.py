""""Please Ask Me"""
def main():
    """Main Function"""
    total = int(input())
    if total >= 8:
        print("Extremely Happy")
    elif total >= 4:
        print("Very Happy")
    elif total >= 1:
        print("Happy")
    else:
        print("Sad")

main()
