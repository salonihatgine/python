'''
@author: Yogeshwar Shukla 
@date: 11th Jan 23 
@goal: To demonstrate: 
        unhandled exception due to error by caller 
'''

def find_max(L:list) -> int: 
    m = L[0]
    i=1 
    while i < len(L): 
        if L[i] > m: 
            m = L[i]
        i = i + 1 
    return m 

L1 = []
find_max(L1)
m1 = find_max(L1)
print("Max in L1 is", m1)



