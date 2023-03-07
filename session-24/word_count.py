import sys

def word_count(s:str)->int:
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
    return (w_cnt)

def main():
    s = input("Enter a string for word couning:")
    w_cnt = word_count(s)
    print("Words in %s = %d" % (s, w_cnt))
    sys.exit(0)

main()
