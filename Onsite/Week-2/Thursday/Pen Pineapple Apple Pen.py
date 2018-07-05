"""Pen Pineapple Apple Pen"""
def main():
    """Main Function"""
    check = 0
    temp = ""
    var = True
    num = 0
    while var:
        text = str(input())
        num += 1
        if text == "Pen" and check == 0:
            check += 1
        if text == "Pineapple" and check == 1:
            check += 1
        if text == "Apple" and check == 2:
            check += 1
        if text == "Pen" and check == 3:
            check += 1

        if check != num and text != "Pen":
            temp = temp + "Wrong lyrics!\n"
            print(check,num,text)
            check = 0
            num = 0


        if check == 4:
            temp = temp + "Correct lyrics!"
            var = False
        print(check, temp)
    print(temp)

main()
