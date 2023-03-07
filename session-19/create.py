
import sys # Package sys import

def main(argc:int,argv:list): #Function Body
    if argc != 2:
        print("Argument count 1 is not valid")
        sys.exit(-1)

    handle = open(argv[1],"w")
    print("Name-Vardhaman",file = handle)
    print("Mobil-8805187108",file = handle)
    handle.close()

    sys.exit(0)

       
main(len(sys.argv),sys.argv) # Function call
    
