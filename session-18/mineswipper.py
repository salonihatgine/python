import sys

def easy_version():
    print("Easu version of mineswipper")

    def intermediate_version():
        print("Intermediate version ofmineswiper")

    def expert_version():
        print("Expert version of mineswipper")

    # sys.argc[0] -> mineswipper.py

    if sys.argv[1] =='-easy':
        easy_version()
    elif sys.argv[1] == '-intermediate':
        intermediate_version()
    elif sysy.argv[1] == '-expert':
        expert_version()
    else:
        print("Invalid option")
        

        