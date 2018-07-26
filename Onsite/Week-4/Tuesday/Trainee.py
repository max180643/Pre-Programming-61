"""Trainee"""
def main():
    """Main Function"""
    jp_n = 0
    kr_n = 0
    jp_list = []
    kr_list = []
    # input
    while True:
        name = input()
        if name == "stop":
            break
        temp = name.split(" ")
        if len(temp) == 2:
            jp_n += 1
            jp_list.append(name)
        elif len(temp) == 3:
            kr_n += 1
            kr_list.append(name)
    # sort
    jp_list = sorted(jp_list)
    kr_list = sorted(kr_list)
    # output
    if jp_n == 0:
        print("No Japanese Trainee")
    else:
        print("%i Japanese Trainee" % (jp_n))
        for i in range(len(jp_list)):
            print(jp_list[i])
    print("----------")
    if kr_n == 0:
        print("No Korean Trainee")
    else:
        print("%i Korean Trainee" % (kr_n))
        for j in range(len(kr_list)):
            print(kr_list[j])

main()
