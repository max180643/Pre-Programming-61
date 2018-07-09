"""Exam Answers"""
def main():
    """Main Function"""
    text1 = input()
    text2 = input()
    score = 0
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            score += 1
    if score == 0:
        print("Pokpak")
    else:
        print("Score : %i/%i" % (score, len(text1)))
        print("%.2f%%" % ((score / len(text1)) * 100))

main()
