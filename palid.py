
def reverse(s):
    return s[::-1]


def palidrome():
    pal = input("Enter the word :")
    s1 = reverse(pal)
    if pal == s1:
        return 1
    else:
        return 0





while True:
    pal=palidrome()
    if pal == 1:
        print("the word is Palidrome")
    else:
        print("the word is mot Palidrome")
