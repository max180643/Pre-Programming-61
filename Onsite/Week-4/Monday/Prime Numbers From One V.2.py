"""Prime Numbers From One V.2"""
def main():
    """Main Function"""
    number = int(input())
    if number > 1:
        for i in range(2, number + 1):
            check = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    check = False
                    break
            if check:
                print(i)

main()
