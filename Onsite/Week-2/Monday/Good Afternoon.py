"""Good Afternoon"""
def main():
    """Main Function"""
    hour = int(input())
    minute = int(input())
    if hour >= 5 and hour < 12 and minute >= 0:
        print("Good Morning")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
    elif hour >= 18 and hour < 23:
        print("Good Evening")
    else:
        print("Good Night")

main()
