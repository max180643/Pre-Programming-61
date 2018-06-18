"""Matrix"""
def main():
    """Main Function"""
    text = ""
    size = int(input())
    for _ in range(size):
        for j in range(size):
            number = int(input())
            text += str(number) + " "
            if j == (size - 1):
                text += "\n"
    print(text)

main()
