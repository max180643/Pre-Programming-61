"""Countdown"""
def main():
    """Main Function"""
    countdown(10)
    countdown(9)
    countdown(8)
    countdown(7)
    countdown(6)
    countdown(5)
    countdown(4)
    countdown(3)
    countdown(2)
    countdown(1)

def countdown(number):
    """Print Countdown"""
    print("- Countdown #%i -" % (number))
    print("New Year in %i..." % (number))

main()
