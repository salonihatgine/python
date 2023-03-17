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
    print("Saloni Hatgine", file=f_handle)
    print("Founder", file=f_handle)
    print("Contact:7410587871", file=f_handle)
    print("salonihatgine108@gmail.com", file=f_handle)
    f_handle.close()

    sys.exit(0)

main(len(sys.argv), sys.argv) 
