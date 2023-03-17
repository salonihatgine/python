import sys 

def main(argc:int, argv:list)->None: 
    '''
    @input: 
    @argc: Argument count 
    @argv: Argument vector 

    Accepts a file name on command line and 
    performs basic create, open, close, read, 
    write operations on the file 
    '''
    
    if argc != 2: 
        print("UsageError:Correct Usage Is:%s file_name" % argv[0])
        sys.exit(-1)

    f_handle = open(argv[1], "w")
    print("Vardhaman Hatgine", file=f_handle)
    print("Student", file=f_handle)
    print("Astromedicomp", file=f_handle)
    print("Contact:8805187108", file=f_handle)
    print("email:hatginev@gmail.com", file=f_handle)
    f_handle.close() 
    
    sys.exit(0) 

main(len(sys.argv), sys.argv)

