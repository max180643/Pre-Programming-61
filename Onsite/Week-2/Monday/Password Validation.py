"""Password Validation"""
def main():
    """Main Function"""
    password = len(input())
    if password < 8:
        print("Password too short, try again.")
    else:
        print("Password is valid, you can use this password.")

main()
