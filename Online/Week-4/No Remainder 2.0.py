"""No Remainder"""
def main():
    """Main Function"""
    var_a = int(input())
    var_b = int(input())
    if var_a > 0:
        var_b = 0 - var_b
    for i in range(var_b * int(var_a / var_b), 0, var_b):
        print(i)

main()
