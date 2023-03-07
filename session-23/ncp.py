import sys

def main(argc:int, argv:list):
    if argc < 3:
        print("UsageError:Correct Usage:%s src_filel src_file2 ... dest_file" %argv[0])
        sys.exit(-1)

    try:
        f_dest_handle = open(argv[argc-1], "w")
    except FileNotFoundError:
        print("System could not locate the specified file %s" % argv[argv-1])
        sys.exit(-1)

    except PermissionError:
        print("The application doesnot have permission to creae file")
        sys.exit(-1)
    except:
        print("Unexpected error in creating the dest file")
        sys.exit()

    i = 1
    while i <= argc-2:
        try:
            f_src_handle = open(argv[i], "r")
        except FileNotFoundError:
            print("Invalid source file %s. skipping it" %argv[i])
            i = i + 1
            continue
        except PermissionError:
            print("Cannot open %s in read mode. Skipping it" % argv[i])
            i = i + 1
            continue
        except:
            print("Unexpeted error in opening %s" % argv[i])
            i = i + 1
            continue
        for line in f_src_handle:
            print(line,file=f_dest_handle, end='')

        f_src_handle.close()
    i = i + 1

    f_dest_handle.close()

    sys.exit(0)

main(len(sys.argv), sys.argv)