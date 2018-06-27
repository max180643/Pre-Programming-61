"""Introduction to Calculus"""
import math as m
def main():
    """Main Function"""
    input1 = int(input())
    input2 = int(input())
    var_a = min(input1, input2)
    var_b = max(input1, input2)
    ans = ((-3 / 2) * m.cos(2 * var_b / 3) - m.sin(var_b) + (4 * var_b)) - \
          ((-3 / 2) * m.cos(2 * var_a / 3) - m.sin(var_a) + (4 * var_a))
    print("%.2f"%(ans))

main()
