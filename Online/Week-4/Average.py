"""Average"""
def main():
    """Main Function"""
    number = int(input())
    avg = 0
    for _ in range(1, number + 1):
        avg += float(input())
    print("Average is %.2f"%(avg / number))

main()
