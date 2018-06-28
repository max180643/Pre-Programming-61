"""Four Dots"""
import math as m
def main():
    """Main Function"""
    a_1 = int(input())
    a_2 = int(input())
    b_1 = int(input())
    b_2 = int(input())
    c_1 = int(input())
    c_2 = int(input())
    d_1 = int(input())
    d_2 = int(input())
    set1 = line(a_1, a_2, b_1, b_2)
    set2 = line(b_1, b_2, c_1, c_2)
    set3 = line(c_1, c_2, d_1, d_2)
    set4 = line(d_1, d_2, a_1, a_2)
    print("%.2f" % (set1 + set2 + set3 + set4))

def line(var_x1, var_y1, var_x2, var_y2):
    """Calculate"""
    ans = m.sqrt((var_x2 - var_x1) ** 2 + (var_y2 - var_y1) ** 2)
    return ans

main()
