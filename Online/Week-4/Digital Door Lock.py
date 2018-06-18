"""Digital Door Lock"""
def main():
    """"Main Function"""
    total = 0
    check = ""
    key = ""
    while key != "-1": # True -> Do loop
        key = input().upper()
        if key == "S":
            check = "S"
        elif key == "E" and check == "S":
            total += 1
            check = ""
    print(total)

main()
