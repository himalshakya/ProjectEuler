import math

# Tests if x is a prime by testing it against a list of primes
def isPrime(x, primeLst):
  for y in primeLst:
    if x % y == 0:
      return False
  return True

def listOfPrimes(x):
  primeList = []
  maxInt = int(math.sqrt(x))
  if x % 2 == 0:
    primeList.append(2)

  for y in range(3, maxInt + 1, 2):
    if x % y == 0:
      if isPrime(y, primeList):
        primeList.append(y)

  return primeList

def problem3(num):
  return max(listOfPrimes(num))

print problem3(600851475143)

