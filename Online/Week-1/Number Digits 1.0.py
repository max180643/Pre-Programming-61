"""Number Digits"""
def main():
    """Main Function"""
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())
    int4 = int(input())
    int5 = int(input())
    # Digit-5
    set1 = int1 / 10
    c_set1 = int(set1)
    m_set1 = c_set1 * 10
    d_set1 = int1 - m_set1
    # Digit-4
    set2 = int2 / 100
    c_set2 = int(set2)
    m_set2 = c_set2 * 100
    d_set2 = int2 - m_set2
    set2_ = d_set2 / 10
    c2_set2 = int(set2_)
    # Digit-3
    set3 = int3 / 1000
    c_set3 = int(set3)
    m_set3 = c_set3 * 1000
    d_set3 = int3 - m_set3
    set3_ = d_set3 / 100
    c3_set3 = int(set3_)
    # Digit-2
    set4 = int4 / 10000
    c_set4 = int(set4)
    m_set4 = c_set4 * 10000
    d_set4 = int4 - m_set4
    set4_ = d_set4 / 1000
    c4_set4 = int(set4_)
    # Digit-1
    set5 = int5 / 100000
    c_set5 = int(set5)
    m_set5 = c_set5 * 100000
    d_set5 = int5 - m_set5
    set5_ = d_set5 / 10000
    c5_set5 = int(set5_)
    # Total
    total = d_set1 + c2_set2 + c3_set3 + c4_set4 + c5_set5
    print("%i+%i+%i+%i+%i = %i"%(d_set1, c2_set2, c3_set3, c4_set4, c5_set5, total))

main()
