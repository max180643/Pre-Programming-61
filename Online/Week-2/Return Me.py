"""Return Me"""
def main():
    """Main Function"""
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())
    print(myfunction())

def myfunction():
    """My Function"""
    num = int(input())
    result = num**4 - num**3 + num**2 - num
    return result

main()
