import time
from decimal import *
getcontext().prec = 1000
#set the digit precision for decimal (10000)

def find_pi_to_nth_digit(nth):
    '''
    Enter the number and have the program generate pi up to that many decimal places
    '''
    
    pi = Decimal(3.0)
    op = 1
    
    for num in range(2,1000000,2):
        pi += 4/Decimal(num*(num+1)*(num+2)*op)
        op *= -1
        
    return round(pi,nth)

reps = int(input("Please enter the number that you want generate pi after decimal: "))

start_time = time.time()

find_pi_to_nth_digit(reps)

end_time = time.time() - start_time
print("The total time taken to run the program is: {}".format(end_time))
