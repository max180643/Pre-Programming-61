"""Prime Number V.2"""
def main(num):
    """Main Function"""
    if num <= 1:
        return "No"
    i = 2
    while i * i <= num:
        if num % i == 0:
            return "No"
        i += 1
    return "Yes"

print(main(int(input())))
