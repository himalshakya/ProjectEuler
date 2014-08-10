#!/usr/bin/python

def nextCollatz(num):
    if num % 2 == 0:
        return num/2
    else:
        return (3*num) + 1

def CollatzSol(mlimit):
    hash = {1: [1]}
    for i in range(1, mlimit):
        j  = i
        stack = []
        loop = True
        while loop:
            if j not in hash:
                stack.append(j)
                j = nextCollatz(j)
            else:
                loop = False
        while len(stack) > 0:
            arrList = list(hash[j])
            j = stack.pop()
            arrList.append(j)
            hash[j] = arrList
    
    maxNum = (-1,-1)
    for x in hash.keys():
        y = len(hash[x])
        if y > maxNum[1]:
            maxNum = (x,y)
    print "MAX :-> ", maxNum
    

CollatzSol(1000000)