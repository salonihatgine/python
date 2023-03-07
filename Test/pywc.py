import sys

def word_count(s:str)->int:
    if type(s) != str:
        raise TypeError("word count requires string input")

    IN = 0
    OUT = 1
    state = OUT
    w_cnt = 0

    for c in s:
        if state == OUT and not c.isspace():
            state = IN
            w_cnt = w_cnt + 1
        elif state == IN and c.isspace():
            state = OUT
    return w_cnt

def main(argc:int, argv:list)->None:

    if argc < 2:
        print("UsageError:%s file1 file2 ..." % argv[0])
        sys.exit(-1)

    nr_total_lines = 0
    nr_total_chars = 0
    nr_total_words = 0

    i = 1
    while i < argc:

        try:
            f_handle = open(argv[i], "r")
        except FileNotFoundError:
            print("Invalid path %s" % argv[1])
            sys.exit(-1)
        except PermissionError:
            print("Permission denied to open %s" % argv[1])
            sys.exit(-1)
        except:
            print("Unexpected error in opening the file %s" % argv[1])
            sys.exit(-1)

        nr_lines = 0
        nr_chars = 0
        nr_words = 0

        for line in f_handle:
            nr_lines = nr_lines + 1
            nr_chars = nr_chars + len(line)
            nr_words = nr_words + word_count(line)
        f_handle.close()
        print(nr_lines, nr_words, nr_chars, argv[i], sep='\t')

        nr_total_chars = nr_total_chars + nr_chars
        nr_total_lines = nr_total_lines + nr_lines
        nr_total_words = nr_total_words + nr_words

        i = i + 1
    
    if argc > 2:
        print(nr_total_lines, nr_total_words, nr_total_chars, "total", sep='\t')

    sys.exit(0)

main(len(sys.argv), sys.argv)

