import math

def isPrime(num):
    ''' isPrime : function that takes a positive integer 1,2,3...n
        returns True or False depending on the num parameter
        Prime Definition : An integer greater than one is called a prime number if its only positive divisors (factors) are one and itself. 
    '''
    if num == 1:
        return False
    if num in [2,3,5,7]:
        return True
    if num%2 == 0:
        return False

    # Condition only for odd natural numbers
    sqrtNum = int(math.sqrt(num)) + 1
    for i in range(3, sqrtNum, 2):
        if num % i == 0:
            return False

    return True

def naturalNumberGenerator():
    current = 1
    while True:
        yield(current)
        current += 1

def problem7(nthNum):
    ''' function problem7 returns the Nth Prime Number
    The nthNum, is the Nth prime number, 2 is the 1st, 3 is the 2nd, onwards
    '''
    count = 0
    current = None
    testGenerator = naturalNumberGenerator()
    while count < nthNum:
        test = next(testGenerator)
        if(isPrime(test)):
            current = test
            count += 1

    return current

