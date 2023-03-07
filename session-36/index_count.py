import sys

def main():

    s = input("Enter the string")
    sub = input("Enter sub string")

    s_index = 0
    indicess = []

    while sub in s[s_index :]:
        ind = s.index(sub.s_index)
        indicess.append(ind)
        s_index = ind + 1

    for i in indicess:
        print(i)

main()
