"""Intermediate Encoder"""

def main():
    """Main Function"""
    num = ord(input())
    if num - 6 == 96:
        num = 122
    elif num - 6 == 95:
        num = 121
    elif num - 6 == 94:
        num = 120
    elif num - 6 == 93:
        num = 119
    elif num - 6 == 92:
        num = 118
    elif num - 6 == 91:
        num = 117
    elif num - 6 == 64:
        num = 90
    elif num - 6 == 63:
        num = 89
    elif num - 6 == 62:
        num = 88
    elif num - 6 == 61:
        num = 87
    elif num - 6 == 60:
        num = 86
    elif num - 6 == 59:
        num = 85
    else:
        num = num - 6
    print(chr(num))

main()
