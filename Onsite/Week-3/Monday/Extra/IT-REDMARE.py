"""IT-REDMARE"""
def main():
    """Main Function"""
    num = int(input())
    line1 = "***** *****     ****  ***** ***   *   *   *   ****  *****\n" * num
    line2 = "  *     *       *   * *     *  *  ** **  * *  *   * *    \n" * num
    line3 = "  *     *   *** ****  ***** *   * * * * ***** ****  *****\n" * num
    line4 = "  *     *       * *   *     *  *  *   * *   * * *   *    \n" * num
    line5 = "*****   *       *  *  ***** ***   *   * *   * *  *  *****\n" * num
    line1 = line1.replace("*", "*" * num)
    line1 = line1.replace(" ", " " * num)
    line2 = line2.replace("*", "*" * num)
    line2 = line2.replace(" ", " " * num)
    line3 = line3.replace("*", "*" * num)
    line3 = line3.replace(" ", " " * num)
    line4 = line4.replace("*", "*" * num)
    line4 = line4.replace(" ", " " * num)
    line5 = line5.replace("*", "*" * num)
    line5 = line5.replace(" ", " " * num)
    print(line1, end="")
    print(line2, end="")
    print(line3, end="")
    print(line4, end="")
    print(line5, end="")

main()
