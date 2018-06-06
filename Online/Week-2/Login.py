"""Login"""
def main():
    """Main Function"""
    username = input()
    password = input()
    password = len(password) * "*"
    print("username : %s"%(username))
    print("password : %s"%(password))

main()
