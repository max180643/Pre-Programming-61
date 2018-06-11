"""Split Function"""
import math
def main():
    """Main Function"""
    var_x = float(input())
    if var_x < 100:
        fx1 = 2 * math.sin((var_x - 10) * math.pi / 180)
    elif var_x > 100:
        fx1 = math.log10(var_x)
    else: # var_x == 100
        fx1 = math.sqrt(var_x) / 5
    print("%.2f" % (fx1))

main()
