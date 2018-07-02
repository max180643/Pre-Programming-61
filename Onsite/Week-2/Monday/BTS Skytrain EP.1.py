"""BTS Skytrain EP.1"""
def main():
    """Main Function"""
    coin = int(input())
    if coin >= 4:
        print("Mo Chit (N8)")
        print("Saphan Khwai (N7)")
    if coin >= 6:
        print("Ari (N5)")
        print("Sanam Pao (N4)")
    if coin >= 7:
        print("Victory Monument (N3)")
    if coin >= 8:
        print("Phaya Thai (N2)")
        print("Ratchathewi (N1)")
    if coin >= 9:
        print("Siam (CEN)")

main()
