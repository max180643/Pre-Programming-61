"""Matrix"""
def main():
    """Main Function"""
    vari = int(input())
    varj = int(input())
    text = ""
    for _ in range(vari):
        for _ in range(varj):
            text += input() + " "
        text += "\n"
    print(text)

main()
