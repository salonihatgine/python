import sys

def main(argc:int, argv:list)-> None:

    if argc != 3:
        print("UsageError:Correct Usage:%s src_file dest_file"% argv[0])
        sys.exit(-1)

    sys.exit(0)

main(len(sys.argv), sys.argv)

