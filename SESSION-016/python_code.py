"""
@Author : Saloni
@Date : 19/12/2022
@Goal : Test
"""
import sys

def main():
    L = []
    while True:
        choice = input("Do Enter integer: [Y-yes|N-No:")
        if choice != 'Y' and choice !='y':
            break
        n = int(input("Enterr by the user:"))
        L.append(n)

    print("Integer entred by tge user:")
    for x in L:
            print(x)

        sys.exit(0)

main()
