import sys

def main(argc:int, argv:list):
    if argc !=3:
        print("UsagError:Usage:%s src_file dest_file" %argv[0])
        sys.exit(-1)

    f_src_handle = open(argv[1], "r")
    f_dest_handle = open(argv[2], "w")

    for line in f_src_handle:
        print(line, file = f_dest_handle, end='')
        
    f_src_handle.close()
    f_dest_handle.close()
    sys.exit(0)

main(len(sys.argv), sys.argv)


