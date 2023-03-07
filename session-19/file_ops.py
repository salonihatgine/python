'''
@author: Saloni Hatgine
@date: 6th JAN 23
@GOAL: To demonstrate following operations on text file
    a) Creat
    b) Write   
    c) Read
    d) Open
    e) Close
    using python bulit in functions(aka high level file handling)

    File name will be accepted from commandline.

    # file_ops.py file_name
 '''

import sys 

def main(argc:int, argv:list)->None:
    '''
    @input:
    @argc: Arument count
    @argv: Argument vector
    
    Accepts a file name on command line and 
    performs basic create, open, close, read,
    write operations on the file
    '''
    if argc != 2:
        print("Usage Error:%s file_name" % argc[0])
        sys.exit(0)

    main(len(sys.argv), sys.argv)

      

