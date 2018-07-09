"""Dog Tag"""
def main():
    """Main Function"""
    name = input()
    print("/--------\\")
    print("|{:^8}|" .format(name[:8]))
    print("\\--------/")

main()
