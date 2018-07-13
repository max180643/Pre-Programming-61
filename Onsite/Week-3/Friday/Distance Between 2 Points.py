"""Distance Between 2 Points"""
import math as m
def main():
    """Main Function"""
    text1 = input()
    text2 = input()
    text1 = text1[1:-1]
    text1 = text1.split(", ")
    text2 = text2[1:-1]
    text2 = text2.split(", ")
    var_x1 = int(text1[0])
    var_y1 = int(text1[1])
    var_x2 = int(text2[0])
    var_y2 = int(text2[1])
    ans = m.sqrt(((var_x2 - var_x1) ** 2) + ((var_y2 - var_y1) ** 2))
    print("%.2f" % (ans))

main()

