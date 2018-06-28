"""Name List"""
def main():
    """Main Function"""
    number = int(input())
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)
    number = info(number)

def info(number):
    """Print Number"""
    print("ID#%i\t%s" % (number, input()))
    print("ID#%i\t%s" % (number+1, input()))
    print("ID#%i\t%s" % (number+2, input()))
    print("ID#%i\t%s" % (number+3, input()))
    print("ID#%i\t%s" % (number+4, input()))
    return number + 5

main()
