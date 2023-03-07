'''
@author: Saloni Hatgine
@date: 18th Jan 2023
@goal: Write a function which acceptes list size
       from end user. The must be between 1 to 15.
       And populate the list by integers also accepted
       from the end user.
'''

import sys

def get_list()-> list:

    min_length = 1
    max_length = 15

    try:
        N = int(input("Enter the length of list[1-15]:"))
        if N < min_length or N > max_length:
            raise ValueError("Size must be between %d and %d" % (min_length, max_length))
    except ValueError as e:
        print(e)
        sys.exit(-1)
    except:
        print("Unexpected error")
        sys.exit(-1)

    L = []
    index = 0
    while index < N:
        try:
            n = int(input("Enter any integer:"))
        except ValueError as e:
            print(e)
            sys.exit(-1)
        except:
            print("unexpected error")
            sys.exit(-1)
        L.append(n) 
        index = index + 1

    return (L)

def main():
    L = get_list()
    print(L)

main()



              