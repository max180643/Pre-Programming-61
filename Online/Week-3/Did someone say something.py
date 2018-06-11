"""Did someone say something?"""
def main():
    """Main Function"""
    sentence = input()
    favorite = input()
    if favorite in sentence:
        print("Did someone say %s?"%(favorite))
    else:
        print("That didn't work.")

main()
