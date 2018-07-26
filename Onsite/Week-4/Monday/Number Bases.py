"""Number Bases"""
def main():
    """Main Function"""
    num = int(input())
    for i in range(2, 37):
        print("Base %i: %s" % (i, convert(num, i)))

def convert(num, base):
    """Convert"""
    convertstring = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num < base:
        return convertstring[num]
    else:
        return convert(num // base, base) + convertstring[num % base]

main()
