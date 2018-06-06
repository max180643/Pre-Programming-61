"""What a Math"""
from math import (cos, radians, sqrt, sin, fabs)
def main():
    """Main Function"""
    var_x = float(input())
    var_a = float(input())
    cut_1 = (var_x * cos(radians(var_a)))
    cut_2 = (sqrt(((var_a ** 3) + sqrt((var_a * sin(radians(60)) + sqrt(var_a))))))
    var_y = cut_1 - cut_2
    print(int(fabs(var_y) * -1))

main()
