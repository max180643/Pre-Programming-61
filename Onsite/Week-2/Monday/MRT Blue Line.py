"""MRT Blue Line"""
def main():
    """Main Function"""
    station = input()
    type_ticket = input()
    # Chatuchak Park
    if station == "Chatuchak Park" and type_ticket == "Adult":
        print("21")
    elif station == "Chatuchak Park" and type_ticket == "Student":
        print("19")
    elif station == "Chatuchak Park" and type_ticket == "Elder":
        print("11")
    # Phahon Yothin
    elif station == "Phahon Yothin" and type_ticket == "Adult":
        print("23")
    elif station == "Phahon Yothin" and type_ticket == "Student":
        print("21")
    elif station == "Phahon Yothin" and type_ticket == "Elder":
        print("12")
    # Lat Phrao
    elif station == "Lat Phrao" and type_ticket == "Adult":
        print("25")
    elif station == "Lat Phrao" and type_ticket == "Student":
        print("23")
    elif station == "Lat Phrao" and type_ticket == "Elder":
        print("13")
    # Ratchadaphisek
    elif station == "Ratchadaphisek" and type_ticket == "Adult":
        print("28")
    elif station == "Ratchadaphisek" and type_ticket == "Student":
        print("25")
    elif station == "Ratchadaphisek" and type_ticket == "Elder":
        print("14")

main()
