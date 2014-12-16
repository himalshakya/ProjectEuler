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

def primeNumberGenerator():
    gen = naturalNumberGenerator()
    while True:
        x = next(gen)
        if (isPrime(x)):
            yield(x)

def problem10(nthNum):
    ''' function problem10 returns the sum of prime numbers less than nthNum
    '''
    testGenerator = primeNumberGenerator()
    sumPrime = 0
    while True:
        prime = next(testGenerator)
        if prime >= nthNum:
            break
        sumPrime += prime

    return sumPrime

