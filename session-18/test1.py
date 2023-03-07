import sys

def easy_level():
    print("Easy Level function")

def intermediate_level():
    print("Intermediate Level function")

def expert_level():
    print("Expert level func tion")

def help():
    print("To select level: mineswipe.py -easy or -intermediate or -expert")
    print("To get help: mineswipe.py -help")

def main(argc:int, argv:list):

    if argc == 1:
        help()
        sys.exit(0)

    if argc > 2:
        print("Invalid command line")
        help()
        sys.exit(-1)

    if argv[1] == '-easy':
        easy_level()

    elif argv[1] == '-itermediate':
        intermediate_level()

    elif argv[1] == '-expert':
        expert_level()
        
    elif argv[1] == 'help':
        help()
    else:
        print("Invalid command argument")
        help()
        sys.exit(-1)

    sys.exit(0)

main(len(sys.argv),sys.argv)