"""Prime Numbers From One"""
import math as m
def main(number):
    """Main Function"""
    for i in range(1, number + 1):
        if check(i) == "Yes":
            print(i)

def check(number):
    """Check"""
    if number < 2:
        return 'No'
    else:
        is_prime = True
        for i in range(2, int(m.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
        if is_prime == True:
            return 'Yes'
        else:
            return 'No'

main(int(input()))
