"""No Remainder"""
def main():
    """Main Function"""
    var_a = int(input())
    var_b = int(input())
    while True:
        check = var_a % var_b
        if var_a == 0:
            break
        if check == 0:
            print(var_a)
        if var_a > 0:
            var_a -= 1
        elif var_a < 0:
            var_a += 1

main()
