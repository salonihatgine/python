import sys

def main(argc:int, argv:list):
    if argc != 2:
        print("UsageError:%s file_path" % argv[0])
        sys.exit(-1)

    try:
        f_handle = open(argv[1], "r")
    except FileNotFoundError:
        print("Invalid path %s" % argv[1])
        sys.exit(-1)
    except PermissionError:
        print("Permision denied to open %s" % argv[1])
        sys.exit(-1)
    except:
        pritn("Unexpected error in opening the %s" % argv[1])
        sys.exit(-1)

    nr_chars = 0
    nr_lines = 0
    for line in f_handle:
        nr_lines = nr_lines + 1
        nr_chars = nr_chars + 1
    f_handle.close()
    print(nr_lines, nr_chars, argv[1], sep='\t')

    sys.exit(0)

main(len(sys.argv), sys.argv)

