"""Is This Calculus"""
import math
def main():
    """Main Function"""
    in1, in2 = float(input()), float(input())
    var_a = (min(in1, in2))
    var_b = (max(in1, in2))
    cal = ((math.pow(var_b, 3) / 3 + var_b) - (math.pow(var_a, 3) / 3 + var_a))
    print("%.2f"%(cal))

main()
