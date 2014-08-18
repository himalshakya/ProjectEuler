def fib(maxnum):
  x = [1,2]
  y = x[len(x) - 2] + x[len(x) - 1]
  while y < maxnum:
    x.append(y)
    y = x[len(x) - 2] + x[len(x) - 1]
  return x

maxvalue = 4 * pow(10,6)

fiboNum = fib(maxvalue)
evenNum = [i for i in fiboNum if i%2 == 0]
print sum(evenNum)
