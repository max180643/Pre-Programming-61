"""Prime Numbers from 1 to n"""
def main():
    """Main Function"""
    num_in = int(input())
    for num in range(num_in + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

main()
