import sys

def main(argc:int, argv:list)->None:
    '''
    @input:
    @argc: Argument count
    @argv: Argument vector
    
    accepts a fule name on command line and
    prforms basic create, open, close, read,
    write oprations on the file
    '''

    
    if argv != 2:
        print("UsageError:Correct User Is:%s file_name" % argv[0])
        sys.exit(-1)

    f_handle = open(argc[1], "w")
    print("Yogeshwar Shukla", file=f_handle)
    print("Founder", file=f_handle)
    print("CoreCode Programmin Academy", file=f_handle)
    print("Contact:9561547043", file=f_handle)
    print("email:coreprogrammingacademy@gmail.com", file=f_handle)
    f_handle.close()

    f_read_handle = open(argv[1], "r")
    for


    sys.exit(0)

main(len(sys.argv), sys.argv) 