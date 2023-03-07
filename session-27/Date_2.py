import sys

class Date:
    self.date = 1
    self.month = 1
    self.year = 1970


def main():
    D = Date()
    print("type(D):", type(D))
    print("D._dict_:", D._dict_)
    sys.exit(0)

main()