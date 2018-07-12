"""Matrix"""
def main():
    """Main Function"""
    num1 = int(input())
    num2 = int(input())
    box = []
    loop = 0
    if num1 > 0:
        for _ in range(num1):
            for _ in range(num2):
                box.append(int(input()))
        size = len(box)
        check = size // num1
        for i in range(size):
            print(str(box[i]) + " ", end="")
            loop += 1
            if loop % check == 0:
                print("")

main()
