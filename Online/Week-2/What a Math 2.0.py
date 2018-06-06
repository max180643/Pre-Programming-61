"""What a Math"""
from math import (cos, radians, sqrt, sin)
def main():
    """Main Function"""
    var_x = float(input())
    var_a = float(input())
    cut_1 = (var_x * cos(radians(var_a)))
    cut_2 = (sqrt(((var_a ** 3) + sqrt((var_a * sin(radians(60)) + sqrt(var_a))))))
    var_y = cut_1 - cut_2
    print(int(((var_y > 0) * (-1 * (var_y * 2))) + var_y))

main()
