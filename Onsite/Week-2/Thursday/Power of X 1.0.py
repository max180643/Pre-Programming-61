"""Power of X"""
def main():
    """"Main Function"""
    number = int(input())
    temp1 = number
    temp2 = 0
    for i in range(1, int(number / 2 + 1)):
        print("%s\\%s/" % (" " * (i - 1), " " * (int(temp1 - 2))))
        temp1 -= 2
    for j in range(int(number / 2 + 1), 1, -1):
        print("%s/%s\\" % (" " * (j - 2), " " * (int(temp2))))
        temp2 += 2

main()
