"""Germany Trip"""
from math import (sqrt, ceil)
def main():
    """Main Function"""
    in_1 = int(input())
    in_2 = int(input())
    in_3 = int(input())
    in_4 = int(input())
    in_5 = int(input())
    in_6 = int(input())
    in_7 = int(input())
    in_8 = int(input())
    in_9 = int(input())
    in_10 = int(input())
    box = 0
    box = box + distant(in_1, in_2, in_3, in_4)
    box = box + distant(in_3, in_4, in_5, in_6)
    box = box + distant(in_5, in_6, in_7, in_8)
    box = box + distant(in_7, in_8, in_9, in_10)
    print(ceil(box))

def distant(x_1, y_1, x_2, y_2):
    """distant"""
    dist = sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    return dist

main()
