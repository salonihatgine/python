import sys

def get_list_of_integers(min_length:int, max_length:int)->list:
    if type (min_length) != int or type(max_length) != int:
        raise TypeError("min and max length parameters must have integer input values")

    if min_length < 0 or max_length <= 0 or min_length > max_length:
        raise ValueError("Wrong bounds for list length")

    try:
        N = int(input("Enter the length of list[%d-%d]" % (min_length, max_length)))
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
            n = int((input("enter any integer at index %d" % index)))
        except ValueError as e:
            print(e)
            sys.exit(-1)
        except:
            print("Unexpected error")
            sys.exit(-1)
        L.append(n)
        index = index + 1

    return (L)

def main():
    L = get_list_of_integers(5, 15)
    print(L)

main()

