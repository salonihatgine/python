def is_prime(n:int)->bool:
    '''
    @input: 
    @n:int: an integer whose primenes whill be tested
    @output:
    True or false Depending on whtger n is prime.
    '''
    if n == 1:
        return False
    if n == 2:
        return True

    flag = True
    k=2
    while k < n:
        if n % k == 0:
            flag = False
        break
    k = k + 1
    return flag

k = 1
while k  <=100:
    print(k, is_prime(k))
    k = k + 1
    



'''
        TODO: Write a main function. Print numbers from 1 to 100 along wiht
        their result of prime test
'''