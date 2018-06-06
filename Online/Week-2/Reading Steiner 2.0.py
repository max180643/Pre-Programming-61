"""Reading Steiner"""
def main():
    """Main function"""
    kit1()

def number():
    """Input"""
    input1 = float(input())
    return input1

def kit1():
    """Kit1"""
    num1 = number() + number()
    num2 = num1 + number()
    num3 = num2 + number()
    num4 = num3 + number()
    num5 = num4 + number()
    num6 = num5 + number()
    num7 = num6 + number()
    num8 = num7 + number()
    num9 = num8 + number()
    num10 = num9 + number()
    text1 = "%.6f\n%.6f\n%.6f\n%.6f\n%.6f\n"%(num1, num2, num3, num4, num5)
    text2 = "%.6f\n%.6f\n%.6f\n%.6f\n%.6f"%(num6, num7, num8, num9, num10)
    text = text1 + text2
    link = kit2(num10)
    print(text)
    print(link)

def kit2(num):
    """Kit2"""
    num11 = num + number()
    num12 = num11 + number()
    num13 = num12 + number()
    num14 = num13 + number()
    num15 = num14 + number()
    num16 = num15 + number()
    num17 = num16 + number()
    num18 = num17 + number()
    num19 = num18 + number()
    num20 = num19 + number()
    text3 = "%.6f\n%.6f\n%.6f\n%.6f\n%.6f\n"%(num11, num12, num13, num14, num15)
    text4 = "%.6f\n%.6f\n%.6f\n%.6f\n%.6f"%(num16, num17, num18, num19, num20)
    text = text3 + text4
    return text

main()
